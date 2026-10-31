import os
from contextlib import contextmanager

import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Import layer-layer yang sudah dibuat
from models.model import Base
from repositories.repository import MahasiswaRepository
from services.service import PrediksiService
from ui import components
from ui.styles import CSS

# 1. Konfigurasi Halaman Web
st.set_page_config(page_title="Sistem Prediksi Kelulusan", page_icon="🎓", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)


@st.cache_resource
def inisialisasi_database() -> sessionmaker:
    load_dotenv()
    url_database = os.getenv("DATABASE_URL", "sqlite:///data_prediksi.db")
    # SQLite + Streamlit: koneksi dipakai lintas thread
    engine = create_engine(url_database, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)


SessionLocal = inisialisasi_database()
service = PrediksiService()


@contextmanager
def sesi_repository():
    """Dependency Injection: satu sesi database per operasi, selalu ditutup."""
    session = SessionLocal()
    try:
        yield MahasiswaRepository(session)
    finally:
        session.close()


# 2. State aplikasi
st.session_state.setdefault("hasil", None)
st.session_state.setdefault("galat_field", {})
st.session_state.setdefault("pesan_galat", "")


def proses_prediksi() -> None:
    """Dipanggil saat tombol ditekan (sebelum halaman digambar ulang)."""
    nama = (st.session_state.get("input_nama") or "").strip()
    ipk = st.session_state.get("input_ipk")
    sks = st.session_state.get("input_sks")

    galat = service.validasi_input(nama, ipk, sks)
    if galat:
        st.session_state.galat_field = galat
        st.session_state.pesan_galat = "Periksa kembali data yang Anda masukkan."
        return

    status = service.tentukan_kelulusan(ipk, sks)
    try:
        with sesi_repository() as repo:
            repo.simpan_data(nama, float(ipk), int(sks), status)
    except SQLAlchemyError:
        st.session_state.galat_field = {}
        st.session_state.pesan_galat = "Data belum dapat disimpan. Silakan coba kembali."
        return

    st.session_state.hasil = {"nama": nama, "status": status}
    st.session_state.galat_field = {}
    st.session_state.pesan_galat = ""
    st.session_state.input_nama = ""
    st.session_state.input_ipk = None
    st.session_state.input_sks = None
    st.toast("Data berhasil disimpan!")


# 3. Ambil data riwayat
with sesi_repository() as repo:
    riwayat = repo.ambil_semua_data()

# 4. Membangun UI (View)
st.markdown(
    components.render_header(len(riwayat), service.hitung_jumlah_lulus(riwayat)),
    unsafe_allow_html=True,
)

kolom_form, kolom_hasil = st.columns([1.15, 0.85], gap="large")
galat_field = st.session_state.galat_field

with kolom_form:
    with st.form("form_input", border=False):
        st.markdown(components.render_judul_form(), unsafe_allow_html=True)

        st.text_input(
            "Nama Mahasiswa",
            key="input_nama",
            max_chars=100,
            placeholder="Contoh: Nabila Putri",
        )
        if "nama" in galat_field:
            st.markdown(components.render_petunjuk(galat_field["nama"], galat=True), unsafe_allow_html=True)

        kolom_ipk, kolom_sks = st.columns(2)
        with kolom_ipk:
            st.number_input(
                "IPK (0.0 - 4.0)",
                key="input_ipk",
                value=None,
                min_value=0.0,
                max_value=4.0,
                step=0.01,
                format="%.2f",
                placeholder="3.50",
            )
            st.markdown(
                components.render_petunjuk(
                    galat_field.get("ipk", "Rentang nilai 0,00–4,00"), galat="ipk" in galat_field
                ),
                unsafe_allow_html=True,
            )
        with kolom_sks:
            st.number_input(
                "Total SKS",
                key="input_sks",
                value=None,
                min_value=0,
                max_value=200,
                step=1,
                placeholder="144",
            )
            st.markdown(
                components.render_petunjuk(
                    galat_field.get("sks", "Maksimal 200 SKS"), galat="sks" in galat_field
                ),
                unsafe_allow_html=True,
            )

        if st.session_state.pesan_galat:
            st.markdown(components.render_peringatan(st.session_state.pesan_galat), unsafe_allow_html=True)

        st.form_submit_button("Prediksi & Simpan  →", on_click=proses_prediksi)

with kolom_hasil:
    st.markdown(components.render_hasil(st.session_state.hasil), unsafe_allow_html=True)

# 5. Riwayat prediksi (tabel) dan footer
st.markdown(components.render_riwayat(riwayat), unsafe_allow_html=True)
st.markdown(components.render_footer(), unsafe_allow_html=True)
