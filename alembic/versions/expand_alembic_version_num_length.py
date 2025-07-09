"""
Expand alembic_version.version_num to VARCHAR(255)

Revision ID: expand_alembic_version_num_length
Revises:
Create Date: 2024-07-09
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "expand_alembic_version_num_length"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE alembic_version
        ALTER COLUMN version_num TYPE VARCHAR(255);
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE alembic_version
        ALTER COLUMN version_num TYPE VARCHAR(32);
        """
    )
