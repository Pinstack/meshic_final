"""
Upgrade parcels_raw.geometry to SRID 3857 (Web Mercator)

Revision ID: upgrade_parcels_raw_geometry_to_3857
Revises:
Create Date: 2024-07-09
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "upgrade_parcels_raw_geometry_to_3857"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # NOTE: This will re-tag existing geometries as 3857, not reproject them.
    op.execute(
        """
        ALTER TABLE parcels_raw
        ALTER COLUMN geometry TYPE geometry(MultiPolygon, 3857)
        USING ST_SetSRID(geometry, 3857);
        """
    )


def downgrade():
    # NOTE: This will re-tag existing geometries as 4326, not reproject them.
    op.execute(
        """
        ALTER TABLE parcels_raw
        ALTER COLUMN geometry TYPE geometry(MultiPolygon, 4326)
        USING ST_SetSRID(geometry, 4326);
        """
    )
