"""empty message

Revision ID: 5daf8c7786a8
Revises: cf79b0bcd9db
Create Date: 2019-08-16 12:08:25.938947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5daf8c7786a8'
down_revision = 'cf79b0bcd9db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###