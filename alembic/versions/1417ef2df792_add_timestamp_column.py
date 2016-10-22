"""Add timestamp column

Revision ID: 1417ef2df792
Revises: 1c5a519ad3ce
Create Date: 2016-10-22 15:13:15.331128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1417ef2df792'
down_revision = '1c5a519ad3ce'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('mood_log', sa.Column('mood', sa.Integer, nullable=False))

def downgrade():
    pass
