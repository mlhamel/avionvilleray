"""adds_events

Revision ID: 1d6d89b1bc
Revises:
Create Date: 2016-03-05 11:10:23.078093

"""

# revision identifiers, used by Alembic.
revision = '1d6d89b1bc'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op

from sqlalchemy import Column, Integer, Unicode


def upgrade():
    op.create_table(
        "events",
        Column("id", Integer, primary_key=True),
        Column("speed", Integer),
        Column("flight", Unicode),
        Column("track", Unicode),
        Column("lat", Integer),
        Column("lon", Integer))


def downgrade():
    op.drop_table("events")
