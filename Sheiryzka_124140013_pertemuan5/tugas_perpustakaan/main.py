"""Program utama: menguji sistem manajemen perpustakaan."""

from library import Library
from library_item import Book, Magazine
from member import Member


def main() -> None:
    """Menjalankan demo: tambah item, katalog, pencarian, peminjaman, pengembalian."""
    perpus = Library("Perpustakaan ITERA")

    print("--- 1. MENAMBAHKAN ITEM ---")
    perpus.tambah_item(Book("B001", "Laskar Pelangi", 2005, "Andrea Hirata", "978-979-3062-79-2", 529))
    perpus.tambah_item(Book("B002", "Bumi Manusia", 1980, "Pramoedya Ananta Toer", "978-979-9731-23-5", 535))
    perpus.tambah_item(Book("B003", "Clean Code", 2008, "Robert C. Martin", "978-0-13-235088-4", 464))
    perpus.tambah_item(Magazine("M001", "National Geographic Indonesia", 2024, "KG Media", "Vol. 20 No. 5"))
    perpus.tambah_item(Magazine("M002", "Tempo", 2025, "PT Tempo Inti Media", "Edisi Oktober"))
    perpus.tambah_item(Book("B001", "Duplikat", 2020, "Anonim", "000", 1))  # ID duplikat
    print(f"Total item di koleksi: {perpus.total_item}")

    print("\n--- 2. MENAMPILKAN KATALOG ---")
    perpus.tampilkan_katalog()

    print("\n--- 3. MENCARI ITEM ---")
    hasil_id = perpus.cari_berdasarkan_id("B003")
    print("Cari ID 'B003'      :", hasil_id)
    print("Cari ID 'X999'      :", perpus.cari_berdasarkan_id("X999"))
    hasil_judul = perpus.cari_berdasarkan_judul("bumi")
    print("Cari judul 'bumi'   :", [item.judul for item in hasil_judul])

    print("\n--- 4. PEMINJAMAN ---")
    hardin = Member("A001", "Malioboro Hartigan")
    tessa = Member("A002", "Alina Resya Prameswari")
    perpus.pinjam_item(hardin, "B001")
    perpus.pinjam_item(tessa, "B001")  # sudah dipinjam
    perpus.pinjam_item(hardin, "M001")
    perpus.pinjam_item(hardin, "B999")  # tidak ada
    print(hardin)

    print("\n--- 5. KATALOG ITEM TERSEDIA ---")
    perpus.tampilkan_katalog(hanya_tersedia=True)

    print("\n--- 6. PENGEMBALIAN & DENDA (POLIMORFISME) ---")
    perpus.kembalikan_item(hardin, "B001", hari_terlambat=5)   # buku: Rp 1.000/hari
    perpus.kembalikan_item(hardin, "M001", hari_terlambat=5)   # majalah: Rp 500/hari
    perpus.kembalikan_item(hardin, "M002")                     # tidak sedang dipinjam
    print(hardin)

    print("\n--- 7. PROTEKSI ENCAPSULATION ---")
    buku = perpus.cari_berdasarkan_id("B002")
    try:
        buku.is_dipinjam = True
    except AttributeError:
        print("Gagal ubah is_dipinjam langsung: property read-only.")
    try:
        buku.tahun_terbit = 3000
    except ValueError as err:
        print(f"Validasi setter tahun_terbit: {err}")


if __name__ == "__main__":
    main()