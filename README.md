# Praktikum RPL 9 - Sistem Prediksi Kelulusan Mahasiswa

Clean Code + SOLID (Single Responsibility), Arsitektur Layered, SQLAlchemy, Streamlit.
Tampilan di-port dari desain Figma / project Next.js "Kampus Insight".

## Arsitektur Layered

```
+--------------------------------------+
| View        app.py + ui/             |  Streamlit, CSS, komponen HTML
+------------------+-------------------+
                   | memanggil
+------------------v-------------------+
| Service     services/service.py      |  Aturan kelulusan + validasi input
+------------------+-------------------+
                   | status
+------------------v-------------------+
| Repository  repositories/repository.py |  Simpan / ambil data
+------------------+-------------------+
                   | memakai
+------------------v-------------------+
| Model       models/model.py          |  Tabel `mahasiswa`
+--------------------------------------+
                   |
             data_prediksi.db (SQLite)
```

## Jalankan

```
pip install -r requirements.txt
streamlit run app.py
```

Catatan: kolom `created_at` baru ditambahkan. Kalau sebelumnya sudah pernah
menjalankan versi lama dan muncul error "no such column: created_at",
hapus file `data_prediksi.db` lalu jalankan ulang.

## Struktur

```
Praktikum_RPL_9/
  app.py                    # View: rangkai UI + dependency injection
  ui/styles.py              # CSS
  ui/components.py          # Potongan HTML (header, hasil, tabel)
  models/model.py
  repositories/repository.py
  services/service.py
  .env                      # DATABASE_URL=sqlite:///data_prediksi.db
  requirements.txt
```
