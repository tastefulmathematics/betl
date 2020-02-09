from core.database import reference_tables, database_binding


class ReferenceInterface:
    _data_source_map = {}
    _subscription_map = {}

    def __init__(self):
        if not self._data_source_map:
            self.cache_data_source_map()
        if not self._subscription_map:
            self.cache_subscription_map()

    def cache_data_source_map(self):
        with database_binding.DatabaseBinding() as conn:
            table = reference_tables.ReferenceTables().data_source
            statement = table.select().order_by(table.c.b_created_by)
            self._data_source_map = {row.key: dict(row) for row in conn.execute(statement)}

    def cache_subscription_map(self):
        with database_binding.DatabaseBinding() as conn:
            table = reference_tables.ReferenceTables().service
            statement = table.select().order_by(table.c.b_created_by)
            service_map = {row.key: dict(row) for row in conn.execute(statement)}

            table = reference_tables.ReferenceTables().topic
            statement = table.select().order_by(table.c.b_created_by)
            topic_map = {row.key: dict(row) for row in conn.execute(statement)}

            table = reference_tables.ReferenceTables().subscription
            statement = table.select().order_by(table.c.b_created_by)
            subscription_map = {row.key: dict(row) for row in conn.execute(statement)}

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

