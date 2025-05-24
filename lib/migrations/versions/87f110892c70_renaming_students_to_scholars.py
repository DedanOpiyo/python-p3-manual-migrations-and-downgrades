"""Renaming students to scholars

Revision ID: 87f110892c70
Revises: 791279dd0760
Create Date: 2025-05-24 12:01:15.838924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87f110892c70'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
