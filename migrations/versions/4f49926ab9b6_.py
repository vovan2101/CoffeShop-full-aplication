"""empty message

Revision ID: 4f49926ab9b6
Revises: 
Create Date: 2022-09-09 20:25:08.547962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f49926ab9b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('items', sa.String(length=25), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('phone_number', sa.String(length=150), nullable=False),
    sa.Column('home_address', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('data_created', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('items', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['items'], ['product.items'], ),
    sa.ForeignKeyConstraint(['price'], ['product.price'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_created', sa.DateTime(), nullable=False),
    sa.Column('items', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['items'], ['product.items'], ),
    sa.ForeignKeyConstraint(['price'], ['product.price'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courier')
    op.drop_table('order')
    op.drop_table('cart')
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_table('user')
    op.drop_table('product')
    # ### end Alembic commands ###
