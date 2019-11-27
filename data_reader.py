import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR.joinpath('data')


class DataReader:

    def read_data_from_file(self, file_format, file_name):
        if file_format == "csv":
            return self.read_csv_file(file_name)
        elif file_format == "json":
            return self.read_json_file(file_name)

    @staticmethod
    def read_csv_file(file_name):
        with open(file_name) as csv_file:
            csv_to_dict = csv.DictReader(csv_file)
            return [row for row in csv_to_dict]

    @staticmethod
    def read_json_file(file_name):
        with open(file_name) as f:
            return json.loads(f.read())

    @staticmethod
    def save_data_to_json_file(data, file_name):
        with open(file_name, 'w') as f:
            f.write(json.dumps(data))


if __name__ == '__main__':
    data_reader = DataReader()

# data_reader.py --file_format=csv --file_name=participants1.csv --number_of_winners=2
