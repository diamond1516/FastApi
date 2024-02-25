"""initial migration

Revision ID: 15b15d5d397b
Revises: 1876514a7153
Create Date: 2024-02-25 19:26:11.210554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15b15d5d397b'
down_revision: Union[str, None] = '1876514a7153'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
