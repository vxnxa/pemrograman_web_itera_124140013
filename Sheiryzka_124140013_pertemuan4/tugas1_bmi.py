"""Tugas 1: Program penghitung BMI (Body Mass Index) sederhana."""


def hitung_bmi(berat: float, tinggi: float) -> float:
    """Menghitung nilai BMI.

    Parameter:
        berat: berat badan dalam kilogram (kg).
        tinggi: tinggi badan dalam meter (m).

    Mengembalikan:
        Nilai BMI (float) dengan rumus berat / (tinggi * tinggi).
    """
    return berat / (tinggi * tinggi)


def tentukan_kategori(bmi: float) -> str:
    """Menentukan kategori berat badan berdasarkan nilai BMI.

    Parameter:
        bmi: nilai BMI yang sudah dihitung.

    Mengembalikan:
        Teks kategori berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def baca_angka_positif(pesan: str) -> float:
    """Meminta input angka positif dari pengguna sampai valid.

    Parameter:
        pesan: teks yang ditampilkan sebagai prompt input.

    Mengembalikan:
        Angka positif (float) yang dimasukkan pengguna.
    """
    while True:
        try:
            nilai = float(input(pesan).replace(",", "."))
            if nilai > 0:
                return nilai
            print("Input harus lebih besar dari 0. Coba lagi.")
        except ValueError:
            print("Input tidak valid, masukkan angka. Coba lagi.")


def main() -> None:
    """Menjalankan program: input data, hitung BMI, tampilkan hasil."""
    print("=== PROGRAM PENGHITUNG BMI ===")
    berat_badan = baca_angka_positif("Masukkan berat badan (kg) : ")
    tinggi_badan = baca_angka_positif("Masukkan tinggi badan (m) : ")

    bmi = hitung_bmi(berat_badan, tinggi_badan)
    kategori = tentukan_kategori(bmi)

    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Berat badan : {berat_badan:.1f} kg")
    print(f"Tinggi badan: {tinggi_badan:.2f} m")
    print(f"Nilai BMI   : {bmi:.2f}")
    print(f"Kategori    : {kategori}")


if __name__ == "__main__":
    main()