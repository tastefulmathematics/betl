import sqlalchemy as sa
import core


class DatabaseBinding:
    """
    Provides access to a databse.  The base context manager uses an engine,
    while also providing DatabaseConnection and DatabaseTransaction optionsS
    """

    def __init__(self, database_key):
        self.connection_string, self.masked_String = core.get_database_url(database_key)
        self.engine = sa.create_engine(self.connection_string)

    def __enter__(self):
        pass

    def __exit__(self, _, _, _):
        self._finalize()

    def __del__(self):
        self._finalize()

    def _finalize(self):
        pass

    def reflect_table(self, table_name, schema_name):
        pass

    def transaction(self):
        pass