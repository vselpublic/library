"""empty message

Revision ID: 5104f7b18a05
Revises: None
Create Date: 2015-06-14 10:54:29.966029

"""

# revision identifiers, used by Alembic.
revision = '5104f7b18a05'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('questionname', sa.String(length=128), nullable=True),
                    sa.Column('text', sa.String(length=999), nullable=True),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_questions_questionname'), 'questions', ['questionname'], unique=False)
    op.create_index(op.f('ix_questions_text'), 'questions', ['text'], unique=False)
    op.create_index(op.f('ix_questions_timestamp'), 'questions', ['timestamp'], unique=False)
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=64), nullable=False),
                    sa.Column('username', sa.String(length=64), nullable=False),
                    sa.Column('password_hash', sa.String(length=128), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('answers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('userid', sa.Integer(), nullable=False),
                    sa.Column('questionid', sa.Integer(), nullable=False),
                    sa.Column('text', sa.String(length=999), nullable=True),
                    sa.Column('likes', sa.Integer(), nullable=True),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['questionid'], ['questions.id'], ),
                    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_answers_likes'), 'answers', ['likes'], unique=False)
    op.create_index(op.f('ix_answers_timestamp'), 'answers', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_answers_timestamp'), table_name='answers')
    op.drop_index(op.f('ix_answers_likes'), table_name='answers')
    op.drop_table('answers')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_questions_timestamp'), table_name='questions')
    op.drop_index(op.f('ix_questions_text'), table_name='questions')
    op.drop_index(op.f('ix_questions_questionname'), table_name='questions')
    op.drop_table('questions')
    ### end Alembic commands ###
