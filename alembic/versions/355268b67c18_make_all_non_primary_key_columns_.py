"""Make all non-primary-key columns nullable for flexibility

Revision ID: 355268b67c18
Revises: 0b9fc0beb271
Create Date: 2025-07-09 15:09:52.691679

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "355268b67c18"
down_revision: Union[str, Sequence[str], None] = "0b9fc0beb271"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("parcels_raw", "tile_id", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("tile_state", "tile_id", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("tile_state", "status", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("tile_state", "status", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("tile_state", "tile_id", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column(
        "parcels_raw", "tile_id", existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###
