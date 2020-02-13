from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa
from core.database import metadata


class ReferenceTables:

    def __init__(self, schema_name="public"):
        self.schema_name = schema_name
        self.metadata = sa.MetaData()
        self.data_source = sa.Table("data_source", self.metadata, *metadata_column_list,
                                    sa.Column("internal_services", JSONB),
                                    sa.Column("external_services", JSONB),
                                    )
        self.service = sa.Table("service", self.metadata, *metadata_column_list)
        self.topic = sa.Table("topic", self.metadata, *metadata_column_list,
                              sa.Column("service_key", sa.Text),
                              )
        self.subscription = sa.Table("subscription", self.metadata, *metadata_column_list,
                                     sa.Column("source_topic_key", sa.Text),
                                     sa.Column("target_topic_key", sa.Text),
                                     sa.Column("protocol_key", sa.Text),
                                     )
