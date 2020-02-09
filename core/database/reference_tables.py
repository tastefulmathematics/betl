from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa
from core.database import metadata


class ReferenceTables:

    def __init__(self, schema_name="public"):
        self.schema_name = schema_name
        self.metadata = sa.MetaData()
        self.data_source = sa.Table("data_source", self.metadata,
                                    sa.Column(**metadata.b_id),
                                    sa.Column(**metadata.b_key),
                                    sa.Column("name", sa.Text),
                                    sa.Column("title", sa.Text),
                                    sa.Column("internal_services", JSONB),
                                    sa.Column("external_services", JSONB),
                                    sa.Column(**metadata.b_options),
                                    sa.Column(**metadata.b_labels),
                                    sa.Column(**metadata.b_created_by),
                                    sa.Column(**metadata.b_created_ts),
                                    )
        self.service = sa.Table("service", self.metadata,
                                sa.Column(**metadata.b_id),
                                sa.Column(**metadata.b_key),
                                sa.Column("name", sa.Text),
                                sa.Column("title", sa.Text),
                                sa.Column(**metadata.b_options),
                                sa.Column(**metadata.b_labels),
                                sa.Column(**metadata.b_created_by),
                                sa.Column(**metadata.b_created_ts),
                                )
        self.topic = sa.Table("topic", self.metadata,
                              sa.Column(**metadata.b_id),
                              sa.Column(**metadata.b_key),
                              sa.Column("service_key", sa.Text),
                              sa.Column("options", JSONB),
                              sa.Column("labels", JSONB),
                              sa.Column(**metadata.b_options),
                              sa.Column(**metadata.b_labels),
                              sa.Column(**metadata.b_created_by),
                              sa.Column(**metadata.b_created_ts),
                              )
        self.subscription = sa.Table("subscription", self.metadata,
                                     sa.Column(**metadata.b_id),
                                     sa.Column(**metadata.b_key),
                                     sa.Column("source_service_key", sa.Text),
                                     sa.Column("source_topic_key", sa.Text),
                                     sa.Column("target_service_key", sa.Text),
                                     sa.Column(**metadata.b_options),
                                     sa.Column(**metadata.b_labels),
                                     sa.Column(**metadata.b_created_by),
                                     sa.Column(**metadata.b_created_ts),
                                     )
