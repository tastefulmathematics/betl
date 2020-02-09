from etl import staging_tables

class StagingInterface:

    def __init__(self. schema_name, daatabase_connection):
        self.schema_name = schema_name
        self.tables = staging_tables.StagingTables(schema_name)
        self.connection = database_connection

    def create_staging_table(table_name, index_fields):
        self.tables.raw_table(table_name, index_tables)
        self.tables.metadata.create(bind=self.connection.engine)

    def create_compact_stging_table(table_name, compact_fields, index_fields):
        table = self.tables.raw_table(table_name, index_tables)
        compact_table = self.tables.compact_table(table_name, compact_fields, inex_fields)
        self.table.metadata.create(bind=self.connectionn.engine)
