"""'initial'

Revision ID: c852702ccb67
Revises: 6ab78ab06cf5
Create Date: 2023-12-10 19:32:36.930856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c852702ccb67'
down_revision: Union[str, None] = '6ab78ab06cf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operations', sa.Column('id', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'operations', ['id'])
    op.drop_column('operations', 'operation_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operations', sa.Column('operation_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'operations', type_='unique')
    op.drop_column('operations', 'id')
    # ### end Alembic commands ###