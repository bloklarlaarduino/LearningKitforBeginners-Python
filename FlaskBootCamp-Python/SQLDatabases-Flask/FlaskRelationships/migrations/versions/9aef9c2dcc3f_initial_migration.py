"""initial migration

Revision ID: 9aef9c2dcc3f
Revises: 
Create Date: 2019-07-12 16:50:32.120078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aef9c2dcc3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ponnies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('ponny_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ponny_id'], ['ponnies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.Text(), nullable=True),
    sa.Column('ponny_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ponny_id'], ['ponnies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toys')
    op.drop_table('owners')
    op.drop_table('ponnies')
    # ### end Alembic commands ###