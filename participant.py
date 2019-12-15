from pathlib import Path

from data_reader import DataReader

BASE_DIR = Path(__file__).resolve().parent
PARTICIPANTS_DIR = BASE_DIR.joinpath('data')


class Participant:
    """Object of Participant method should contains loaded from file data about the participants"""

    def __init__(self, file_name, file_format="json"):
        self.file_format = file_format
        self.file_name = file_name

    def read_data_from_file(self):
        if self.file_format == "csv":
            return DataReader.read_csv_file(f"{PARTICIPANTS_DIR}/{self.file_name}")
        elif self.file_format == "json":
            return DataReader.read_json_file(f"{PARTICIPANTS_DIR}/{self.file_name}")
        else:
            raise Exception(f"File format {self.file_format} is unknown")


if __name__ == '__main__':
    participant_csv = Participant("participants1.csv", "csv")
    print(participant_csv.read_data_from_file())
    participant_json = Participant("participants1.json", "json")
    print(participant_json.read_data_from_file())

# data_reader.py --file_format=csv --file_name=participants1.csv --number_of_winners=2
