from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa
from core.database import metadata


class TransformerTables:

    def __init__(self, schema_name="public"):
        self.schema_name = schema_name
        self.metadata = sa.MetaData()
        self.transformer = sa.Table("transformer", self.metadata, *metadata_column_list)
