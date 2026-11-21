from setuptools import find_packages, setup


setup(
    name="pyramid-mahasiswa",
    version="0.1.0",
    description="RESTful API mahasiswa dan mata kuliah dengan Pyramid",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "alembic>=1.13,<2",
        "psycopg2-binary>=2.9,<3",
        "pyramid>=2.0,<3",
        "pyramid-tm>=2.5,<3",
        "SQLAlchemy>=2.0,<3",
        "waitress>=3.0,<4",
        "zope.sqlalchemy>=3.1,<4",
    ],
    entry_points={
        "paste.app_factory": [
            "main = pyramid_mahasiswa:main",
        ],
    },
)
