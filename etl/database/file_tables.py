import sqlalchemy as sa
from core import metadata_columns


class FileTables:

    def __init__(self, schema_name="public"):
        self.schema_name = schema_name
        self.metadata = sa.MetaData()
        self.file = sa.Table("file", self.metadata, *metadata_column_list,
            sa.Column("data_source_key", sa.Text),
            sa.Column("system_key", sa.Text),
        )
        self.file_directory = sa.Table("file_directory", self.metadata, *metadata_column_list,
            sa.Column("data_source_key", sa.Text),
            sa.Column("system_key", sa.Text),
        )
