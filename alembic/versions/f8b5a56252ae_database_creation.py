"""Database creation

Revision ID: f8b5a56252ae
Revises: 
Create Date: 2023-07-21 14:14:13.410686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b5a56252ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'menus',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=250), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id')
    )

    op.create_table(
        'submenus',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=250), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('menu_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id')
    )

    op.create_table(
        'dishes',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=250), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('submenu_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['submenu_id'], ['submenus.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dishes')
    op.drop_table('submenus')
    op.drop_table('menus')
    # ### end Alembic commands ###
