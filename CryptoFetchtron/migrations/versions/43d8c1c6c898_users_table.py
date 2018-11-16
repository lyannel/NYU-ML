"""users table

Revision ID: 43d8c1c6c898
Revises: 
Create Date: 2018-11-10 23:16:04.417070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43d8c1c6c898'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crypto__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Coin_Name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_crypto__data_Coin_Name'), 'crypto__data', ['Coin_Name'], unique=True)
    op.create_table('price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Quantity', sa.Integer(), nullable=True),
    sa.Column('Price', sa.Integer(), nullable=True),
    sa.Column('Date', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('price')
    op.drop_index(op.f('ix_crypto__data_Coin_Name'), table_name='crypto__data')
    op.drop_table('crypto__data')
    # ### end Alembic commands ###