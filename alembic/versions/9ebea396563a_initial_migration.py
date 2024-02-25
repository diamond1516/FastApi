"""initial migration

Revision ID: 9ebea396563a
Revises: 15b15d5d397b
Create Date: 2024-02-25 19:26:13.657524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ebea396563a'
down_revision: Union[str, None] = '15b15d5d397b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
