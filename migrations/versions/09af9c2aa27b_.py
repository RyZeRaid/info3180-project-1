"""empty message

Revision ID: 09af9c2aa27b
Revises: 
Create Date: 2022-03-20 17:14:42.867356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09af9c2aa27b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=700), nullable=True),
    sa.Column('num_rooms', sa.Integer(), nullable=True),
    sa.Column('num_bathrooms', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('prop_type', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo_name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
