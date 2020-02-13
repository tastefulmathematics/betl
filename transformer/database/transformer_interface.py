import datetime

from core.database import reference_interface
from etl import file_tables


class TransformerInterface(ReferenceInterface):
    _transformer_map = {}

    def __init__(self, user):
        super(TransformerInterface).__init__(self, user)
        if not self._transformer_map:
            self.cache_transformer_map()
        self.user = user

    def cache_file_directory_map():
        with database_binding.DatabaseBinding() as conn:
            table = transformer_tables.TransformerTables().transformer
            self._transformer_map = self.compactify_table(table)
