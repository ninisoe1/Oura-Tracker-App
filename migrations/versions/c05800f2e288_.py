"""empty message

Revision ID: c05800f2e288
Revises: 6602efc94587
Create Date: 2022-09-27 17:46:30.079488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c05800f2e288'
down_revision = '6602efc94587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_workout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day_num', sa.Integer(), nullable=True),
    sa.Column('template_name', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('workout_params', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['template_name'], ['template.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'day', ['id'])
    op.add_column('template', sa.Column('starting_prs', sa.JSON(), nullable=True))
    op.add_column('template', sa.Column('current_prs', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('template', 'current_prs')
    op.drop_column('template', 'starting_prs')
    op.drop_constraint(None, 'day', type_='unique')
    op.drop_table('base_workout')
    # ### end Alembic commands ###
