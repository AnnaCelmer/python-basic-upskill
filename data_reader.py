import csv
import json


class DataReader:
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
