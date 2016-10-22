"""create mood table

Revision ID: 1c5a519ad3ce
Revises: 
Create Date: 2016-10-22 15:03:43.881682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c5a519ad3ce'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
            'mood_log',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
            )

def downgrade():
    pass
