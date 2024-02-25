"""initial migration

Revision ID: 1817d635b2ff
Revises: 9ebea396563a
Create Date: 2024-02-25 19:27:03.050293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1817d635b2ff'
down_revision: Union[str, None] = '9ebea396563a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
