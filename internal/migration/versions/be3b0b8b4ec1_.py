"""empty message

Revision ID: be3b0b8b4ec1
Revises: 503584ff31e8
Create Date: 2024-12-15 16:13:20.629299

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'be3b0b8b4ec1'
down_revision = '503584ff31e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_config', schema=None) as batch_op:
        batch_op.add_column(sa.Column('suggested_after_answer', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text('\'{"enable": true}\'::jsonb'), nullable=False))

    with op.batch_alter_table('app_config_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('suggested_after_answer', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text('\'{"enable": true}\'::jsonb'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_config_version', schema=None) as batch_op:
        batch_op.drop_column('suggested_after_answer')

    with op.batch_alter_table('app_config', schema=None) as batch_op:
        batch_op.drop_column('suggested_after_answer')

    # ### end Alembic commands ###