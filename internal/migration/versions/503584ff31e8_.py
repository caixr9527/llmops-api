"""empty message

Revision ID: 503584ff31e8
Revises: a27bbc6d11fa
Create Date: 2024-11-25 23:01:20.474854

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '503584ff31e8'
down_revision = 'a27bbc6d11fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_config',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('app_id', sa.UUID(), nullable=False),
    sa.Column('model_config', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('dialog_round', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('preset_prompt', sa.Text(), server_default=sa.text("''::text"), nullable=False),
    sa.Column('tools', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('workflows', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('retrieval_config', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('long_term_memory', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('opening_statement', sa.Text(), server_default=sa.text("''::text"), nullable=False),
    sa.Column('opening_questions', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('speech_to_text', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('text_to_speech', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('review_config', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_app_config_id')
    )
    op.create_table('app_config_version',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('app_id', sa.UUID(), nullable=False),
    sa.Column('model_config', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('dialog_round', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('preset_prompt', sa.Text(), server_default=sa.text("''::text"), nullable=False),
    sa.Column('tools', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('workflows', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('datasets', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('retrieval_config', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('long_term_memory', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('opening_statement', sa.Text(), server_default=sa.text("''::text"), nullable=False),
    sa.Column('opening_questions', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=False),
    sa.Column('speech_to_text', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('text_to_speech', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('review_config', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column('version', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('config_type', sa.String(length=255), server_default=sa.text("''::character varying"), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_app_config_version_id')
    )
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.add_column(sa.Column('app_config_id', sa.UUID(), nullable=True))
        batch_op.add_column(sa.Column('draft_app_config_id', sa.UUID(), nullable=True))
        batch_op.add_column(sa.Column('debug_conversation_id', sa.UUID(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False))
        batch_op.alter_column('account_id',
               existing_type=sa.UUID(),
               nullable=False)
        batch_op.drop_index('idx_app_account_id')
        batch_op.drop_column('update_at')
        batch_op.drop_column('create_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('update_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.create_index('idx_app_account_id', ['account_id'], unique=False)
        batch_op.alter_column('account_id',
               existing_type=sa.UUID(),
               nullable=True)
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('debug_conversation_id')
        batch_op.drop_column('draft_app_config_id')
        batch_op.drop_column('app_config_id')

    op.drop_table('app_config_version')
    op.drop_table('app_config')
    # ### end Alembic commands ###