"""Program utama: menguji seluruh fungsi pada modul math_operations."""

# Cara impor 1: mengimpor seluruh modul (dipanggil dengan awalan nama modul)
import math_operations

# Cara impor 2: mengimpor fungsi/konstanta tertentu langsung ke namespace
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin, PI

# Cara impor 3: mengimpor modul dengan alias
import math_operations as mo


def garis(judul: str) -> None:
    """Mencetak judul bagian dengan garis pembatas.

    Parameter:
        judul: teks judul bagian.
    """
    print(f"\n{'=' * 8} {judul} {'=' * 8}")


def uji_geometri() -> None:
    """Menguji fungsi luas dan keliling untuk persegi, persegi panjang, lingkaran."""
    garis("GEOMETRI")

    for sisi in (4, 7.5):
        print(f"Persegi (sisi={sisi})")
        print(f"  Luas    : {math_operations.luas_persegi(sisi):.2f}")
        print(f"  Keliling: {math_operations.keliling_persegi(sisi):.2f}")

    for panjang, lebar in ((10, 5), (8.5, 3.2)):
        print(f"Persegi panjang (p={panjang}, l={lebar})")
        print(f"  Luas    : {math_operations.luas_persegi_panjang(panjang, lebar):.2f}")
        print(f"  Keliling: {math_operations.keliling_persegi_panjang(panjang, lebar):.2f}")

    for jari_jari in (7, 10.5):
        print(f"Lingkaran (r={jari_jari}, PI={PI})")
        print(f"  Luas    : {mo.luas_lingkaran(jari_jari):.2f}")
        print(f"  Keliling: {mo.keliling_lingkaran(jari_jari):.2f}")


def uji_suhu() -> None:
    """Menguji fungsi konversi suhu dari Celsius."""
    garis("KONVERSI SUHU")
    print(f"{'Celsius':>10}{'Fahrenheit':>14}{'Kelvin':>10}")
    for celsius in (0, 25, 37, 100):
        fahrenheit = celsius_ke_fahrenheit(celsius)
        kelvin = celsius_ke_kelvin(celsius)
        print(f"{celsius:>9}C{fahrenheit:>13.2f}F{kelvin:>9.2f}K")


def main() -> None:
    """Menjalankan seluruh pengujian modul."""
    print("=== PENGUJIAN MODUL math_operations ===")
    uji_geometri()
    uji_suhu()


if __name__ == "__main__":
    main()