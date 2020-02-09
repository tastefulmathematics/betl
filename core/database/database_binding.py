import sqlalchemy as sa
from core import facade


class DatabaseBinding:
    """
    Provides access to a databse.  The base context manager uses an engine,
    while also providing DatabaseConnection and DatabaseTransaction optionsS
    """

    def __init__(self, database_key):
        self.connection_string, self.masked_String = facade.get_database_url(database_key)
        self.engine = sa.create_engine(self.connection_string)

    def __enter__():
        pass

    def __exit__():
        pass

    def __del__():
        pass

    def reflect_table(table_name, schema_name):
        pass
