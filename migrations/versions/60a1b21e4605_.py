"""empty message

Revision ID: 60a1b21e4605
Revises: 4f8b78199d09
Create Date: 2020-09-05 14:24:30.801311

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60a1b21e4605'
down_revision = '4f8b78199d09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job__post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(length=1000), nullable=False),
    sa.Column('job_description', sa.String(length=2000), nullable=False),
    sa.Column('job_address', sa.String(length=120), nullable=False),
    sa.Column('job_zipcode', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('address', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('first_name', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('type_of_user', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('zipcode', sa.String(length=10), nullable=False))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user', 'zipcode')
    op.drop_column('user', 'type_of_user')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'address')
    op.drop_table('job__post')
    # ### end Alembic commands ###