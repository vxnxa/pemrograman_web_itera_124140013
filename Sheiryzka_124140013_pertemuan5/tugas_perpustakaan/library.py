"""Modul perpustakaan: mengelola koleksi LibraryItem dan proses peminjaman."""

from library_item import LibraryItem
from member import Member


class Library:
    """Perpustakaan yang menyimpan dan mengelola koleksi item.

    Atribut:
        _nama (protected): nama perpustakaan.
        __koleksi (private): dictionary {item_id: LibraryItem}.
    """

    def __init__(self, nama: str):
        """Membuat perpustakaan baru.

        Parameter:
            nama: nama perpustakaan.
        """
        self._nama = nama
        self.__koleksi = {}

    @property
    def total_item(self) -> int:
        """Jumlah seluruh item dalam koleksi."""
        return len(self.__koleksi)

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan item ke koleksi.

        Parameter:
            item: objek turunan LibraryItem.

        Mengembalikan:
            True jika berhasil, False jika ID sudah terdaftar.
        """
        if item.item_id in self.__koleksi:
            print(f"Gagal: ID {item.item_id} sudah terdaftar.")
            return False
        self.__koleksi[item.item_id] = item
        print(f"Berhasil menambahkan: {item.judul} ({item.item_id})")
        return True

    def tampilkan_katalog(self, hanya_tersedia: bool = False) -> None:
        """Menampilkan daftar item (polimorfik via get_detail()).

        Parameter:
            hanya_tersedia: jika True, hanya tampilkan item yang tidak dipinjam.
        """
        judul = "KATALOG ITEM TERSEDIA" if hanya_tersedia else "KATALOG LENGKAP"
        print(f"\n===== {judul} - {self._nama} =====")
        ditampilkan = 0
        for item in self.__koleksi.values():
            if hanya_tersedia and item.is_dipinjam:
                continue
            print(item.get_detail())
            ditampilkan += 1
        if ditampilkan == 0:
            print("(tidak ada item)")

    def cari_berdasarkan_id(self, item_id: str):
        """Mencari item berdasarkan ID.

        Parameter:
            item_id: kode item yang dicari.

        Mengembalikan:
            Objek LibraryItem, atau None jika tidak ditemukan.
        """
        return self.__koleksi.get(item_id)

    def cari_berdasarkan_judul(self, kata_kunci: str) -> list:
        """Mencari item yang judulnya mengandung kata kunci (tidak peka huruf besar/kecil).

        Parameter:
            kata_kunci: potongan judul yang dicari.

        Mengembalikan:
            List objek LibraryItem yang cocok.
        """
        kata_kunci = kata_kunci.lower()
        return [item for item in self.__koleksi.values() if kata_kunci in item.judul.lower()]

    def pinjam_item(self, member: Member, item_id: str) -> bool:
        """Memproses peminjaman item oleh anggota.

        Parameter:
            member: anggota yang meminjam.
            item_id: kode item yang dipinjam.

        Mengembalikan:
            True jika peminjaman berhasil.
        """
        item = self.cari_berdasarkan_id(item_id)
        if item is None:
            print(f"Gagal: item {item_id} tidak ditemukan.")
            return False
        if not member.bisa_meminjam():
            print(f"Gagal: {member.nama} sudah mencapai batas {Member.MAKS_PINJAM} pinjaman.")
            return False
        if not item.pinjam():
            print(f"Gagal: '{item.judul}' sedang dipinjam.")
            return False
        member.tambah_pinjaman(item)
        print(f"{member.nama} berhasil meminjam '{item.judul}'.")
        return True

    def kembalikan_item(self, member: Member, item_id: str, hari_terlambat: int = 0) -> bool:
        """Memproses pengembalian item dan menghitung denda bila terlambat.

        Parameter:
            member: anggota yang mengembalikan.
            item_id: kode item yang dikembalikan.
            hari_terlambat: jumlah hari keterlambatan (0 jika tepat waktu).

        Mengembalikan:
            True jika pengembalian berhasil.
        """
        item = self.cari_berdasarkan_id(item_id)
        if item is None or item not in member.daftar_pinjam:
            print(f"Gagal: {member.nama} tidak sedang meminjam item {item_id}.")
            return False
        item.kembalikan()
        member.hapus_pinjaman(item)
        denda = item.hitung_denda(hari_terlambat)  # polimorfik
        print(f"{member.nama} mengembalikan '{item.judul}'. Denda: Rp {denda:,}")
        return True