"""Roles

Revision ID: 0c56770dfefa
Revises: f7d10b00843b
Create Date: 2022-07-26 08:49:43.035389

"""
from alembic import op

from Tables import Role

# revision identifiers, used by Alembic.
revision = '0c56770dfefa'
down_revision = 'f7d10b00843b'
branch_labels = None
depends_on = None

roles_table = Role.__table__


def upgrade():
    op.execute(
        roles_table.insert().values([
            {
                'role': 'root'
            },
            {
                'role': 'admin'
            }
        ])
    )


def downgrade():
    op.execute(
        roles_table.delete()
    )
