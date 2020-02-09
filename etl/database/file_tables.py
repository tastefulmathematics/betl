import sqlalchemy as sa
from core import metadata_columns


class FileTables:

    def __init__(self, schema_name="public"):
        self.schema_name = schema_name
        self.metadata = sa.MetaData()
        self.file = sa.Table("file", self.metadata,
            sa.Column(**metadata_columns.b_id),
            sa.Column(**metadata_columns.b_key),
            sa.Column("name", sa.Text),
            sa.Column("title", sa.Text),
            sa.Column("data_source_key", sa.Text),
            sa.Column("system_key", sa.Text),
            sa.Column("options", JSONB),
            sa.Column("labels", Array),
            sa.Column(**metadata_columns.b_is_valid),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
            sa.Column(**metadata_columns.b_touched_by),
            sa.Column(**metadata_columns.b_touched_ts),
        )
        self.file_direcory = sa.Table("file_direcotry", self.metadata,
            sa.Column(**metadata_columns.b_id),
            sa.Column(**metadata_columns.b_key),
            sa.Column("name", sa.Text),
            sa.Column("title", sa.Text),
            sa.Column("data_source_key", sa.Text),
            sa.Column("system_key", sa.Text),
            sa.Column("options", JSONB),
            sa.Column("labels", Array),
            sa.Column(**metadata_columns.b_is_valid),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
            sa.Column(**metadata_columns.b_touched_by),
            sa.Column(**metadata_columns.b_touched_ts),
        )
        self.file_route = sa.Table("file_route", self.metadata,
            sa.Column(**metadata_columns.b_id),
            sa.Column(**metadata_columns.b_key),
            sa.Column("file_drectory_key", sa.Text),
            sa.Column("options", JSONB),
            sa.Column(**metadata_columns.b_is_valid),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
            sa.Column(**metadata_columns.b_touched_by),
            sa.Column(**metadata_columns.b_touched_ts),
        )
