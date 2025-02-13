"""empty message

Revision ID: 46366fb01814
Revises: 640ec69b3dc5
Create Date: 2025-01-23 21:02:38.844052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46366fb01814'
down_revision: Union[str, None] = '640ec69b3dc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_age'), 'users', ['age'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_age'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    # ### end Alembic commands ###
