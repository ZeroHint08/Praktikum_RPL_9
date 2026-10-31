"""Komponen tampilan (HTML) untuk View Layer. Tidak ada logika bisnis di sini."""
import html
from datetime import datetime

from services.service import (
    BATAS_IPK_MINIMAL,
    BATAS_SKS_MINIMAL,
    STATUS_LULUS,
)

BULAN_SINGKAT = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
                 "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


def rapikan(markup: str) -> str:
    """Hapus indentasi supaya Markdown tidak menganggap HTML sebagai blok kode."""
    return " ".join(baris.strip() for baris in markup.splitlines())


def format_tanggal(nilai: datetime | None) -> str:
    if nilai is None:
        return "-"
    return f"{nilai.day:02d} {BULAN_SINGKAT[nilai.month - 1]} {nilai.year}"


def render_header(total: int, jumlah_lulus: int) -> str:
    return rapikan(f"""
    <div class="kp-header">
      <div>
        <div class="kp-brand">
          <div class="kp-logo">K</div>
          <span class="kp-brand-name">Kampus Insight</span>
          <span class="kp-sep"></span>
          <span class="kp-brand-sub">Academic Tools</span>
        </div>
        <p class="kp-eyebrow">Prediksi akademik</p>
        <h1 class="kp-title">Sistem Prediksi Kelulusan</h1>
        <p class="kp-subtitle">Evaluasi kesiapan kelulusan mahasiswa secara cepat
        berdasarkan capaian IPK dan jumlah SKS.</p>
      </div>
      <div class="kp-stats">
        <div class="kp-stat">
          <p class="kp-stat-num">{total}</p>
          <p class="kp-stat-label">Total prediksi</p>
        </div>
        <div class="kp-stat teal">
          <p class="kp-stat-num">{jumlah_lulus}</p>
          <p class="kp-stat-label">Tepat waktu</p>
        </div>
      </div>
    </div>
    """)


def render_judul_form() -> str:
    return rapikan("""
    <div class="kp-card-head">
      <div>
        <p class="kp-eyebrow">Data akademik</p>
        <h2 class="kp-card-title">Masukkan data mahasiswa</h2>
        <p class="kp-card-desc">Isi data dengan benar untuk mendapatkan hasil prediksi kelulusan.</p>
      </div>
      <div class="kp-icon">🎓</div>
    </div>
    """)


def render_petunjuk(teks: str, galat: bool = False) -> str:
    kelas = "kp-hint err" if galat else "kp-hint"
    return f'<p class="{kelas}">{html.escape(teks)}</p>'


def render_peringatan(pesan: str) -> str:
    return f'<div class="kp-alert" role="alert">{html.escape(pesan)}</div>'


def render_hasil(hasil: dict | None) -> str:
    batas = rapikan(f"""
    <div class="kp-limits">
      <div class="kp-limit"><p class="kp-limit-num">≥ {BATAS_IPK_MINIMAL:.2f}</p><p class="kp-limit-label">Batas IPK</p></div>
      <div class="kp-limit"><p class="kp-limit-num">≥ {BATAS_SKS_MINIMAL}</p><p class="kp-limit-label">Batas SKS</p></div>
    </div>
    """)

    if hasil is None:
        kelas, ikon = "", "🎓"
        isi = rapikan("""
        <p class="kp-result-status" style="max-width:20rem">Siap melihat potensi kelulusan?</p>
        <p class="kp-result-text">Hasil akan tampil di sini setelah data diproses dan otomatis tersimpan ke riwayat.</p>
        """)
    else:
        lulus = hasil["status"] == STATUS_LULUS
        kelas, ikon = ("lulus" if lulus else "tidak"), "✓"
        keterangan = (
            "Mahasiswa memenuhi batas minimal IPK dan total SKS untuk lulus tepat waktu."
            if lulus
            else "Mahasiswa belum memenuhi salah satu batas minimal kelulusan tepat waktu."
        )
        isi = rapikan(f"""
        <p class="kp-muted">Hasil untuk</p>
        <h3 class="kp-result-name">{html.escape(hasil["nama"])}</h3>
        <div class="kp-divider"></div>
        <p class="kp-result-status">{html.escape(hasil["status"])}</p>
        <p class="kp-result-text">{keterangan}</p>
        """)

    return rapikan(f"""
    <div class="kp-result {kelas}">
      <div class="kp-result-top">
        <p class="kp-result-eyebrow">Hasil prediksi</p>
        <span class="kp-result-badge">{ikon}</span>
      </div>
      <div class="kp-result-body">{isi}</div>
      {batas}
    </div>
    """)


def _render_baris(item) -> str:
    lulus = item.status_kelulusan == STATUS_LULUS
    kelas = "lulus" if lulus else "tidak"
    nama = item.nama or ""
    inisial = html.escape(nama[:1].upper())
    return rapikan(f"""
    <tr>
      <td><div class="kp-student"><span class="kp-avatar">{inisial}</span>
        <span class="kp-student-name">{html.escape(nama)}</span></div></td>
      <td class="kp-num">{item.ipk:.2f}</td>
      <td class="kp-num" style="font-weight:500">{item.sks} SKS</td>
      <td><span class="kp-status {kelas}"><span class="kp-dot"></span>{html.escape(item.status_kelulusan)}</span></td>
      <td class="kp-date">{format_tanggal(item.created_at)}</td>
    </tr>
    """)


def render_riwayat(riwayat) -> str:
    if riwayat:
        baris = "".join(_render_baris(item) for item in riwayat)
        isi = rapikan(f"""
        <div class="kp-table-wrap"><table class="kp-table">
          <thead><tr><th>Mahasiswa</th><th>IPK</th><th>Total SKS</th><th>Status</th><th>Tanggal</th></tr></thead>
          <tbody>{baris}</tbody>
        </table></div>
        """)
    else:
        isi = rapikan("""
        <div class="kp-empty">
          <div class="kp-empty-icon">0</div>
          <h3>Belum ada riwayat prediksi</h3>
          <p>Isi formulir di atas untuk membuat prediksi pertama.</p>
        </div>
        """)

    return rapikan(f"""
    <section class="kp-section">
      <div class="kp-section-head">
        <div>
          <p class="kp-eyebrow">Data tersimpan</p>
          <h2 class="kp-card-title">Riwayat Prediksi</h2>
        </div>
        <span class="kp-pill-count">{len(riwayat)} entri terbaru</span>
      </div>
      {isi}
    </section>
    """)


def render_footer() -> str:
    return rapikan("""
    <div class="kp-footer">
      <p>Modul Praktikum 9 · Rekayasa Perangkat Lunak</p>
      <p>Clean Code · SOLID · Layered Architecture</p>
    </div>
    """)
