import argparse
import sys

from pyramid.paster import bootstrap, setup_logging

from ..models import Matakuliah


INITIAL_COURSES = (
    {"kode_mk": "IF25-21008", "nama_mk": "Jaringan Komputer", "sks": 3, "semester": 3},
    {"kode_mk": "IF25-22014", "nama_mk": "Pengembangan Aplikasi Web", "sks": 3, "semester": 5},
    {
        "kode_mk": "IF25-31023",
        "nama_mk": "Manajemen Proyek Teknologi Informasi",
        "sks": 3,
        "semester": 5,
    },
)


def setup_models(dbsession):
    """Insert initial courses without duplicating existing course codes."""
    inserted = 0
    for course_data in INITIAL_COURSES:
        exists = (
            dbsession.query(Matakuliah)
            .filter_by(kode_mk=course_data["kode_mk"])
            .first()
        )
        if exists is None:
            dbsession.add(Matakuliah(**course_data))
            inserted += 1
    return inserted


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("config_uri", help="Configuration file, e.g. development.ini")
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)
    try:
        with env["request"].tm:
            inserted = setup_models(env["request"].dbsession)
        print(f"Seeding selesai: {inserted} mata kuliah baru ditambahkan.")
    finally:
        env["closer"]()


if __name__ == "__main__":
    main()
