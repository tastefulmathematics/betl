import datetime

from core.database import reference_interface
from etl import file_tables


class FileInterface(ReferenceInterface):
    _file_directory_map = {}

    def __init__(self, user):
        super(FileInterface).__init__(self)
        if not self._file_directory_map:
            self.cache_file_directory_map()
        self.user = user

    def cache_file_directory_map():
        with database_binding.DatabaseBinding() as conn:
            table = file_tables.FileTables().file_directory
            self._data_source_map = self.compactify_table(table)

    def store_file(self, file_location):
        directory_key = file_location.rpartition("/")[0]
        created_ts = datetime.datetime.utcnow()
        file_record = {
            "key": file_location,
            "directory_key": directory_key,
            "b_created_by": self.user,
            "b_created_ts": created_ts,
        }

        if directory_key not in self._file_directory_map:
            file_directory_record = {
                "key": directory_key,
                "b_created_by": self.user,
                "b_created_ts": created_ts,
            }
            return False
        else:
            return self._file_directory_map[directory_key]
