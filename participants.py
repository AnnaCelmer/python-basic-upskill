from pathlib import Path

from data_reader import read_csv_file, read_json_file

PARTICIPANTS_DIR = Path.cwd() / 'data'


class Participants:
    """Object of Participant method should contains loaded from file data about the participants"""

    @staticmethod
    def read_data_from_file(file_name, file_format="json"):
        if file_format == "csv":
            return read_csv_file(f"{PARTICIPANTS_DIR}/{file_name}")
        elif file_format == "json":
            return read_json_file(f"{PARTICIPANTS_DIR}/{file_name}")
        else:
            raise Exception(f"File format {file_name} is unknown")
