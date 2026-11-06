"""Tugas 2: Program pengelolaan data nilai mahasiswa."""

BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BOBOT_TUGAS = 0.30

data_mahasiswa = [
    {"nama": "Ryan Imran", "nim": "124140001", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
    {"nama": "Sarah Nasyla Imran", "nim": "124140002", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 80},
    {"nama": "Malioboro Hartigan", "nim": "124140003", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 70},
    {"nama": "Marcello Este", "nim": "124140004", "nilai_uts": 55, "nilai_uas": 50, "nilai_tugas": 60},
    {"nama": "Jivana Putri Kirana", "nim": "124140005", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50},
    {"nama": "Naomi Rachel Agiesta", "nim": "124140006", "nilai_uts": 95, "nilai_uas": 92, "nilai_tugas": 98},
]


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """Menghitung nilai akhir dengan bobot 30% UTS, 40% UAS, 30% Tugas.

    Parameter:
        uts: nilai ujian tengah semester.
        uas: nilai ujian akhir semester.
        tugas: nilai tugas.

    Mengembalikan:
        Nilai akhir (float).
    """
    return (BOBOT_UTS * uts) + (BOBOT_UAS * uas) + (BOBOT_TUGAS * tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade huruf dari nilai akhir.

    Parameter:
        nilai_akhir: nilai akhir mahasiswa.

    Mengembalikan:
        Grade "A", "B", "C", "D", atau "E".
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def proses_data(daftar: list) -> list:
    """Menambahkan kunci nilai_akhir dan grade ke setiap data mahasiswa.

    Parameter:
        daftar: list berisi dictionary data mahasiswa.

    Mengembalikan:
        List dictionary baru yang sudah dilengkapi nilai akhir dan grade.
    """
    hasil = []
    for mhs in daftar:
        nilai_akhir = hitung_nilai_akhir(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
        hasil.append({**mhs, "nilai_akhir": nilai_akhir, "grade": tentukan_grade(nilai_akhir)})
    return hasil


def tampilkan_tabel(daftar: list) -> None:
    """Mencetak data mahasiswa dalam format tabel yang rapi.

    Parameter:
        daftar: list dictionary mahasiswa yang sudah memiliki nilai_akhir dan grade.
    """
    garis = "-" * 78
    print(garis)
    print(f"{'No':<4}{'Nama':<25}{'NIM':<12}{'UTS':>6}{'UAS':>6}{'Tugas':>7}{'Akhir':>10}{'Grade':>8}")
    print(garis)
    for no, mhs in enumerate(daftar, start=1):
        print(
            f"{no:<4}{mhs['nama']:<25}{mhs['nim']:<12}"
            f"{mhs['nilai_uts']:>6}{mhs['nilai_uas']:>6}{mhs['nilai_tugas']:>7}"
            f"{mhs['nilai_akhir']:>10.2f}{mhs['grade']:>8}"
        )
    print(garis)


def tampilkan_info(judul: str, mhs: dict) -> None:
    """Mencetak informasi singkat seorang mahasiswa.

    Parameter:
        judul: label informasi, misalnya "Nilai Tertinggi".
        mhs: dictionary data mahasiswa.
    """
    print(f"{judul:<16}: {mhs['nama']} ({mhs['nim']}) - "
          f"Nilai Akhir {mhs['nilai_akhir']:.2f}, Grade {mhs['grade']}")


def main() -> None:
    """Menjalankan program: proses data, tampilkan tabel, cari tertinggi/terendah."""
    print("=== DATA NILAI MAHASISWA ===")
    mahasiswa = proses_data(data_mahasiswa)
    tampilkan_tabel(mahasiswa)

    tertinggi = max(mahasiswa, key=lambda m: m["nilai_akhir"])
    terendah = min(mahasiswa, key=lambda m: m["nilai_akhir"])

    print()
    tampilkan_info("Nilai Tertinggi", tertinggi)
    tampilkan_info("Nilai Terendah", terendah)


if __name__ == "__main__":
    main()