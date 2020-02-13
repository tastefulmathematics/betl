import core
from core.database import reference_tables, database_binding


class ReferenceInterface:
    _data_source_map = {}
    _subscription_map = {}

    def __init__(self):
        if not self._data_source_map:
            self.cache_data_source_map()
        if not self._subscription_map:
            self.cache_subscription_map()

    def compactify_table(self, table):
        with database_binding.DatabaseBinding("default_reference_database") as conn:
            statement = table.select().order_by(table.c.b_created_ts)
            default_table = {row.key: dict(row) for row in conn.execute(statement)}

        if core.is_production():
            return default_table

        with database_binding.DatabaseBinding("reference_database") as conn:
            statement = table.select().order_by(table.c.b_created_ts)
            override_table = {row.key: dict(row) for row in conn.execute(statement)}
            default_table.update(override_table)
            return default_table

    def cache_data_source_map(self):
        with database_binding.DatabaseBinding() as conn:
            table = reference_tables.ReferenceTables().data_source
            self._data_source_map = self.compactify_table(table)

    def cache_subscription_map(self):
        with database_binding.DatabaseBinding() as conn:
            table = reference_tables.ReferenceTables().service
            service_map = self.compactify_table(table)

            table = reference_tables.ReferenceTables().topic
            topic_map = self.compactify_table(table)

            table = reference_tables.ReferenceTables().subscription
            subscription_map = self.compactify_table(table)

            for subscription_record in subscription_map.values():
                topic_key = subscription_record["topic_key"]
                topic_record = topic_map[topic_key]

                source_service_key = topic_record["service_key"]
                source_service_record = service_map[source_service_key]

                target_service_key = subscription_record["service_key"]
                target_service_record = service_map[target_service_key]

                self._subscription_map[(topic_key, target_service_key)] = {
                    "source_service": source_service_record,
                    "target_service": target_service_record,
                    "topic": topic_record,
                    "subscription": subscription_record,
                    "strategy": subscription_record["strategy"],
                }
