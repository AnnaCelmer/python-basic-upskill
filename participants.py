from pathlib import Path

from data_reader import read_csv_file, read_json_file

PARTICIPANTS_DIR = Path.cwd() / 'data'


class Participants:
    def __init__(self):
        self.list_of_participants = []

    def read_data_from_file(self, file_name, file_format="json"):
        if file_format == "csv":
            self.list_of_participants = read_csv_file(f"{PARTICIPANTS_DIR}/{file_name}.{file_format}")
        elif file_format == "json":
            self.list_of_participants = read_json_file(f"{PARTICIPANTS_DIR}/{file_name}.{file_format}")
        else:
            raise Exception(f"File format {file_name} is unknown")
        return self.list_of_participants
