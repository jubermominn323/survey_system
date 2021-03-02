"""empty message

Revision ID: dda0b253577e
Revises: 395bdd46578e
Create Date: 2020-12-17 11:53:32.561432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda0b253577e'
down_revision = '395bdd46578e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('form', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('form', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.add_column('option', sa.Column('choice_text', sa.String(), nullable=True))
    op.add_column('option', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('option', sa.Column('params', sa.String(), nullable=True))
    op.add_column('option', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.drop_column('option', 'ch_text')
    op.add_column('question', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('question', sa.Column('params', sa.String(), nullable=True))
    op.add_column('question', sa.Column('question_type', sa.String(), nullable=True))
    op.add_column('question', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.drop_column('question', 'que_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('que_type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('question', 'updated_on')
    op.drop_column('question', 'question_type')
    op.drop_column('question', 'params')
    op.drop_column('question', 'created_on')
    op.add_column('option', sa.Column('ch_text', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('option', 'updated_on')
    op.drop_column('option', 'params')
    op.drop_column('option', 'created_on')
    op.drop_column('option', 'choice_text')
    op.drop_column('form', 'updated_on')
    op.drop_column('form', 'created_on')
    # ### end Alembic commands ###
