import sqlalchemy as sa
from core import metadata_columns


class EnterpriseTables:

    def __init__(self, schema_name="public"):
        self.schema_name = schema_name
        self.metadata = sa.MetaData()
        self.error_message = sa.Table("error_message", self.metadata,
            sa.Column(**metadata_columns.b_id),
            sa.Column("target", sa.Text),
            sa.Column("message", JSONB),
            sa.Column("error_data", JSONB),
            sa.Column("state", sa.Text),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
            sa.Column(**metadata_columns.b_touched_by),
            sa.Column(**metadata_columns.b_touched_ts),
        )
        self.message_log = sa.Table("message_log", self.metadata,
            sa.Column(**metadata_columns.b_id),
            sa.Column("target", sa.Text),
            sa.Column("message", JSONB),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
        )
