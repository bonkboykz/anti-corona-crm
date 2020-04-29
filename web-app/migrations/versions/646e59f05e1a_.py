"""empty message

Revision ID: 646e59f05e1a
Revises: fab9bd53103a
Create Date: 2020-04-29 07:57:39.107877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '646e59f05e1a'
down_revision = 'fab9bd53103a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.create_table('JobCategory',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
        sa.UniqueConstraint('value')
        )
    except Exception as e:
        print("Message:", e)
    op.add_column('Patient', sa.Column('job_category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Patient', 'JobCategory', ['job_category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Patient', type_='foreignkey')
    op.drop_column('Patient', 'job_category_id')
    op.drop_table('JobCategory')
    # ### end Alembic commands ###