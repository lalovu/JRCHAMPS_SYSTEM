"""Add email field to StudentInfo model

Revision ID: a77a117a3569
Revises: ad8046b9363f
Create Date: 2024-07-15 03:02:01.416294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a77a117a3569'
down_revision = 'ad8046b9363f'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_info', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)

    # ### end Alembic commands ###