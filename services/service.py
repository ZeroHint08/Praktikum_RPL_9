# Clean Code: konstanta yang jelas, tidak ada magic numbers
BATAS_IPK_MINIMAL = 3.0
BATAS_SKS_MINIMAL = 140
IPK_MAKSIMAL = 4.0
SKS_MAKSIMAL = 200
NAMA_MAKSIMAL_KARAKTER = 100

STATUS_LULUS = "Lulus Tepat Waktu"
STATUS_TIDAK_LULUS = "Tidak Lulus"


class PrediksiService:
    def tentukan_kelulusan(self, ipk: float, sks: int) -> str:
        if ipk >= BATAS_IPK_MINIMAL and sks >= BATAS_SKS_MINIMAL:
            return STATUS_LULUS
        return STATUS_TIDAK_LULUS

    def validasi_input(self, nama: str, ipk, sks) -> dict:
        """Kembalikan dict {field: pesan}. Dict kosong berarti input valid."""
        galat = {}

        nama_bersih = (nama or "").strip()
        if not nama_bersih:
            galat["nama"] = "Nama mahasiswa wajib diisi."
        elif len(nama_bersih) > NAMA_MAKSIMAL_KARAKTER:
            galat["nama"] = f"Nama maksimal {NAMA_MAKSIMAL_KARAKTER} karakter."

        if ipk is None or not 0 <= ipk <= IPK_MAKSIMAL:
            galat["ipk"] = "IPK harus berada di antara 0,00 dan 4,00."

        sks_bulat = sks is not None and float(sks).is_integer()
        if not sks_bulat or not 0 <= sks <= SKS_MAKSIMAL:
            galat["sks"] = f"Total SKS harus berupa bilangan bulat 0–{SKS_MAKSIMAL}."

        return galat

    def hitung_jumlah_lulus(self, riwayat) -> int:
        return sum(1 for item in riwayat if item.status_kelulusan == STATUS_LULUS)
