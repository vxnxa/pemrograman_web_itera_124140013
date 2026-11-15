# Tugas Praktikum Pertemuan 5: Python OOP

## Identitas
- Nama : Sheiryzka Revania Maharani
- NIM  : 124140013
- Kelas: RA

## Deskripsi Program
Sistem manajemen perpustakaan sederhana berbasis OOP Python. Pengguna dapat
menambahkan item (buku dan majalah) ke perpustakaan, menampilkan katalog,
mencari item berdasarkan judul atau ID, meminjam dan mengembalikan item
(dengan perhitungan denda), serta melihat status ketersediaan item.

### Struktur File (`tugas_perpustakaan/`)
- `library_item.py`: abstract class `LibraryItem`, subclass `Book` dan `Magazine`
- `member.py`: class `Member` (anggota perpustakaan)
- `library.py`: class `Library` (pengelola koleksi dan peminjaman)
- `main.py`: program utama untuk menguji seluruh fitur

### Penerapan Pilar OOP
- **Class dan Object**: `Library`, `Member`, `Book`, `Magazine` diinstansiasi
  sebagai objek di `main.py`.
- **Abstraction dan Inheritance**: `LibraryItem(ABC)` adalah abstract class
  dengan abstract method `get_detail()` dan `hitung_denda()`. `Book` dan
  `Magazine` mewarisi `LibraryItem` dan wajib mengimplementasikan keduanya.
- **Encapsulation**: atribut `__dipinjam`, `__tahun_terbit` (private),
  `_item_id`, `_judul` (protected), dan `__koleksi` di `Library` (private)
  tidak diubah langsung dari luar class. Property `is_dipinjam` bersifat
  read-only, dan `tahun_terbit` memakai getter-setter dengan validasi.
- **Polymorphism**: `tampilkan_katalog()` memanggil `get_detail()` dan
  `kembalikan_item()` memanggil `hitung_denda()` pada objek yang berbeda
  tipe. Hasilnya berbeda sesuai class masing-masing (denda buku Rp 1.000
  per hari, majalah Rp 500 per hari).

## Fitur
- Menambahkan item (tolak ID duplikat)
- Menampilkan katalog lengkap dan katalog item yang tersedia
- Mencari item berdasarkan ID atau judul
- Meminjam dan mengembalikan item (batas 3 pinjaman per anggota)
- Perhitungan denda keterlambatan

## Cara Menjalankan
Pastikan Python 3.10+ terpasang, lalu buka terminal di folder repositori:

```bash
cd tugas_perpustakaan
python main.py
```

(Gunakan `python3` atau `py` jika `python` tidak dikenali.)

## Screenshot Output
![Output 1](screenshots/output1.png)
![Output 2](screenshots/output2.png)