"""Create the mahasiswa table.

Revision ID: 20261121_mahasiswa
Revises:
Create Date: 2026-11-21
"""
from alembic import op
import sqlalchemy as sa


revision = "20261121_mahasiswa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "mahasiswa",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nim", sa.Text(), nullable=False),
        sa.Column("nama", sa.Text(), nullable=False),
        sa.Column("jurusan", sa.Text(), nullable=False),
        sa.Column("tanggal_lahir", sa.Date(), nullable=True),
        sa.Column("alamat", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nim"),
    )


def downgrade():
    op.drop_table("mahasiswa")
