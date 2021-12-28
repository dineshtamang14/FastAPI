"""add few columns to posts table

Revision ID: 75082af165cd
Revises: d5f9d5bcc566
Create Date: 2021-12-28 14:58:32.936196

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '75082af165cd'
down_revision = 'd5f9d5bcc566'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),
                  op.add_column('posts', sa.Column(
                      'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'),
                  )))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
