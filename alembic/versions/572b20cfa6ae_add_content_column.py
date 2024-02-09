"""add content column

Revision ID: 572b20cfa6ae
Revises: 7ab63295894c
Create Date: 2024-02-08 12:28:53.023127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '572b20cfa6ae'
down_revision: Union[str, None] = '7ab63295894c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
