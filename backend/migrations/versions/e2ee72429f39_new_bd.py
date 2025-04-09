"""new bd

Revision ID: e2ee72429f39
Revises: cc8402d4a969
Create Date: 2025-04-08 22:34:51.841663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e2ee72429f39'
down_revision = 'cc8402d4a969'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('users', 'surname')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'age')
    op.drop_column('users', 'interests')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('interests', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('gender', postgresql.ENUM('MALE', 'FEMALE', 'OTHER', name='genderenum'), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('users', 'is_verified')
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###
