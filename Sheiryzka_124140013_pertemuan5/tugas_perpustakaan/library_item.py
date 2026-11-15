"""Modul item perpustakaan: abstract class LibraryItem beserta subclass Book dan Magazine."""

from abc import ABC, abstractmethod
from datetime import datetime


class LibraryItem(ABC):
    """Abstract class dasar untuk semua item di perpustakaan.

    Atribut:
        _item_id (protected): kode unik item.
        _judul (protected): judul item.
        __tahun_terbit (private): tahun terbit, divalidasi lewat property.
        __dipinjam (private): status peminjaman, hanya diubah lewat pinjam()/kembalikan().
    """

    def __init__(self, item_id: str, judul: str, tahun_terbit: int):
        """Membuat item perpustakaan baru.

        Parameter:
            item_id: kode unik item (contoh: "B001").
            judul: judul item.
            tahun_terbit: tahun terbit item.
        """
        self._item_id = item_id
        self._judul = judul
        self.__tahun_terbit = 0
        self.tahun_terbit = tahun_terbit  # lewat setter agar divalidasi
        self.__dipinjam = False

    # ---------- Property ----------
    @property
    def item_id(self) -> str:
        """Kode unik item (read-only)."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Judul item (read-only)."""
        return self._judul

    @property
    def tahun_terbit(self) -> int:
        """Tahun terbit item."""
        return self.__tahun_terbit

    @tahun_terbit.setter
    def tahun_terbit(self, nilai: int):
        """Mengatur tahun terbit dengan validasi rentang tahun."""
        if not isinstance(nilai, int) or nilai < 1000 or nilai > datetime.now().year:
            raise ValueError(f"Tahun terbit tidak valid: {nilai}")
        self.__tahun_terbit = nilai

    @property
    def is_dipinjam(self) -> bool:
        """Status peminjaman item (read-only dari luar class)."""
        return self.__dipinjam

    # ---------- Method konkret (dibagi ke semua subclass) ----------
    def pinjam(self) -> bool:
        """Menandai item sebagai dipinjam.

        Mengembalikan:
            True jika berhasil, False jika item sedang dipinjam.
        """
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Menandai item sebagai sudah dikembalikan.

        Mengembalikan:
            True jika berhasil, False jika item memang tidak sedang dipinjam.
        """
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    # ---------- Method abstract (wajib di-override subclass) ----------
    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan teks detail lengkap item."""

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> int:
        """Menghitung denda keterlambatan.

        Parameter:
            hari_terlambat: jumlah hari keterlambatan.

        Mengembalikan:
            Total denda dalam rupiah.
        """

    def __str__(self) -> str:
        """Representasi ringkas item beserta status ketersediaan."""
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"{self._item_id} | {self._judul} ({self.__tahun_terbit}) | {status}"


class Book(LibraryItem):
    """Buku: item perpustakaan dengan penulis, ISBN, dan jumlah halaman."""

    DENDA_PER_HARI = 1000

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 penulis: str, isbn: str, jumlah_halaman: int):
        """Membuat objek buku.

        Parameter:
            item_id, judul, tahun_terbit: diteruskan ke LibraryItem.
            penulis: nama penulis buku.
            isbn: nomor ISBN buku.
            jumlah_halaman: jumlah halaman buku.
        """
        super().__init__(item_id, judul, tahun_terbit)
        self._penulis = penulis
        self._isbn = isbn
        self._jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        """Detail buku: penulis, ISBN, dan jumlah halaman."""
        return (f"[BUKU] {self}\n"
                f"        Penulis: {self._penulis} | ISBN: {self._isbn} | {self._jumlah_halaman} halaman")

    def hitung_denda(self, hari_terlambat: int) -> int:
        """Denda buku: Rp 1.000 per hari keterlambatan."""
        return max(0, hari_terlambat) * self.DENDA_PER_HARI


class Magazine(LibraryItem):
    """Majalah: item perpustakaan dengan penerbit dan edisi."""

    DENDA_PER_HARI = 500

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 penerbit: str, edisi: str):
        """Membuat objek majalah.

        Parameter:
            item_id, judul, tahun_terbit: diteruskan ke LibraryItem.
            penerbit: nama penerbit majalah.
            edisi: edisi majalah (contoh: "Vol. 12 No. 3").
        """
        super().__init__(item_id, judul, tahun_terbit)
        self._penerbit = penerbit
        self._edisi = edisi

    def get_detail(self) -> str:
        """Detail majalah: penerbit dan edisi."""
        return (f"[MAJALAH] {self}\n"
                f"        Penerbit: {self._penerbit} | Edisi: {self._edisi}")

    def hitung_denda(self, hari_terlambat: int) -> int:
        """Denda majalah: Rp 500 per hari keterlambatan."""
        return max(0, hari_terlambat) * self.DENDA_PER_HARI