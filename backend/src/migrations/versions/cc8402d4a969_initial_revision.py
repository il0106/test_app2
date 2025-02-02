"""Initial revision

Revision ID: cc8402d4a969
Revises: 347351c66fd1
Create Date: 2025-02-02 14:38:21.897107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cc8402d4a969'
down_revision = '347351c66fd1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'gender',
               existing_type=postgresql.ENUM('MALE', 'FEMALE', 'OTHER', name='genderenum'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'gender',
               existing_type=postgresql.ENUM('MALE', 'FEMALE', 'OTHER', name='genderenum'),
               nullable=False)
    # ### end Alembic commands ###
