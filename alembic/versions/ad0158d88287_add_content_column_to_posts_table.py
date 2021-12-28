"""add content column to posts table

Revision ID: ad0158d88287
Revises: 500ac510ef72
Create Date: 2021-12-28 14:15:13.421586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad0158d88287'
down_revision = '500ac510ef72'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
