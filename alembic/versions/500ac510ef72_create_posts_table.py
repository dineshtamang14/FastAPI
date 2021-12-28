"""create posts table

Revision ID: 500ac510ef72
Revises: 
Create Date: 2021-12-28 14:02:32.093560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500ac510ef72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
