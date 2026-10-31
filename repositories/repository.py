from sqlalchemy.orm import Session

from models.model import Mahasiswa

BATAS_RIWAYAT = 100


class MahasiswaRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def simpan_data(self, nama: str, ipk: float, sks: int, status: str) -> Mahasiswa:
        # Clean Code: Nama variabel jelas
        data_baru = Mahasiswa(nama=nama, ipk=ipk, sks=sks, status_kelulusan=status)
        self.db.add(data_baru)
        self.db.commit()
        self.db.refresh(data_baru)
        return data_baru

    def ambil_semua_data(self, batas: int = BATAS_RIWAYAT) -> list[Mahasiswa]:
        # Data terbaru tampil paling atas
        return (
            self.db.query(Mahasiswa)
            .order_by(Mahasiswa.created_at.desc(), Mahasiswa.id.desc())
            .limit(batas)
            .all()
        )
