import datetime

from core.database import reference_interface
from etl import file_tables


class FileInterface:

    def __init__(self, user):
        self.user = user

    def store_file(self, file_location):
        directory_key = file_location.rpartition("/")[0]
        created_ts = datetime.datetime.utcnow()
        file_record = {
            "key": file_location,
            "directory_key": directory_key,
            "b_created_by": self.user,
            "b_created_ts": created_ts,
        }

        file_directory_record = {
            "key": directory_key,
            "b_created_by": self.user,
            "b_created_ts": created_ts,
        }
