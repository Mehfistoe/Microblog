"""followers

Revision ID: 792ce59723c2
Revises: bcf3c1a4d8ef
Create Date: 2019-12-27 14:24:47.371813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '792ce59723c2'
down_revision = 'bcf3c1a4d8ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
