from pathlib import Path

from data_reader import DataReader

BASE_DIR = Path(__file__).resolve().parent
PARTICIPANTS_DIR = BASE_DIR.joinpath('data')


class Participant:
    """Object of Participant method should contains loaded from file data about the participants"""

    def __init__(self, file_name):
        self.file_name = file_name if "." in file_name else f"{file_name}.json"

    def read_data_from_file(self):
        if "csv" in self.file_name:
            return DataReader.read_csv_file(f"{PARTICIPANTS_DIR}/{self.file_name}")
        elif "json" in self.file_name:
            return DataReader.read_json_file(f"{PARTICIPANTS_DIR}/{self.file_name}")
        else:
            raise Exception(f"File format {self.file_name} is unknown")

