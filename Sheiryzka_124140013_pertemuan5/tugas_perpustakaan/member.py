"""Modul anggota perpustakaan."""


class Member:
    """Anggota perpustakaan yang dapat meminjam item.

    Atribut:
        _member_id (protected): ID anggota.
        _nama (protected): nama anggota.
        __daftar_pinjam (private): item yang sedang dipinjam anggota.
    """

    MAKS_PINJAM = 3

    def __init__(self, member_id: str, nama: str):
        """Membuat anggota baru.

        Parameter:
            member_id: ID unik anggota.
            nama: nama lengkap anggota.
        """
        self._member_id = member_id
        self._nama = nama
        self.__daftar_pinjam = []

    @property
    def member_id(self) -> str:
        """ID anggota (read-only)."""
        return self._member_id

    @property
    def nama(self) -> str:
        """Nama anggota (read-only)."""
        return self._nama

    @property
    def daftar_pinjam(self) -> list:
        """Salinan daftar item yang sedang dipinjam (aman dari modifikasi luar)."""
        return list(self.__daftar_pinjam)

    def bisa_meminjam(self) -> bool:
        """True jika jumlah pinjaman belum mencapai batas maksimal."""
        return len(self.__daftar_pinjam) < self.MAKS_PINJAM

    def tambah_pinjaman(self, item) -> None:
        """Mencatat item yang dipinjam anggota.

        Parameter:
            item: objek LibraryItem yang dipinjam.
        """
        self.__daftar_pinjam.append(item)

    def hapus_pinjaman(self, item) -> None:
        """Menghapus item dari daftar pinjaman anggota.

        Parameter:
            item: objek LibraryItem yang dikembalikan.
        """
        if item in self.__daftar_pinjam:
            self.__daftar_pinjam.remove(item)

    def __str__(self) -> str:
        """Representasi ringkas anggota."""
        return f"{self._member_id} | {self._nama} | Pinjaman: {len(self.__daftar_pinjam)}/{self.MAKS_PINJAM}"