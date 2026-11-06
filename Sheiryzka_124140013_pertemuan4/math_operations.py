"""Modul operasi matematika: geometri dan konversi suhu."""

PI = 3.14159


# ---------- Geometri: Persegi ----------
def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Parameter:
        sisi: panjang sisi persegi.

    Mengembalikan:
        Luas persegi (sisi * sisi).
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Parameter:
        sisi: panjang sisi persegi.

    Mengembalikan:
        Keliling persegi (4 * sisi).
    """
    return 4 * sisi


# ---------- Geometri: Persegi Panjang ----------
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Parameter:
        panjang: panjang persegi panjang.
        lebar: lebar persegi panjang.

    Mengembalikan:
        Luas persegi panjang (panjang * lebar).
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Parameter:
        panjang: panjang persegi panjang.
        lebar: lebar persegi panjang.

    Mengembalikan:
        Keliling persegi panjang (2 * (panjang + lebar)).
    """
    return 2 * (panjang + lebar)


# ---------- Geometri: Lingkaran ----------
def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran.

    Parameter:
        jari_jari: jari-jari lingkaran.

    Mengembalikan:
        Luas lingkaran (PI * jari_jari^2).
    """
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling lingkaran.

    Parameter:
        jari_jari: jari-jari lingkaran.

    Mengembalikan:
        Keliling lingkaran (2 * PI * jari_jari).
    """
    return 2 * PI * jari_jari


# ---------- Konversi Suhu ----------
def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Fahrenheit.

    Parameter:
        celsius: suhu dalam derajat Celsius.

    Mengembalikan:
        Suhu dalam Fahrenheit (C * 9/5 + 32).
    """
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Kelvin.

    Parameter:
        celsius: suhu dalam derajat Celsius.

    Mengembalikan:
        Suhu dalam Kelvin (C + 273.15).
    """
    return celsius + 273.15


if __name__ == "__main__":
    print("[TEST MODUL] Luas lingkaran r=7:", luas_lingkaran(7))