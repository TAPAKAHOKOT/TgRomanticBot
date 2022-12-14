"""add messages soft-delete

Revision ID: cf2edd594185
Revises: 4d4953a5e297
Create Date: 2022-11-13 14:02:22.992930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf2edd594185'
down_revision = '4d4953a5e297'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('status', sa.String(), server_default='active', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'status')
    # ### end Alembic commands ###
