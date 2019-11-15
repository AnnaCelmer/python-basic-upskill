import json
import csv
import random
from configuration import args

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR.joinpath('data')


class DataReader:

    def print_all_winners(self, file_format, file_name, number_of_winners):
        data = self.read_data_from_file(file_format, file_name)
        winners = random.sample(data, number_of_winners)
        for winner in winners:
            print("The winner is %s %s" % (winner["first_name"], winner["last_name"]))

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


if __name__ == '__main__':
    data_reader = DataReader()
    data_reader.print_all_winners(file_format=args.file_format, file_name=f'{TEMPLATES_DIR}/{args.file_name}',
                                  number_of_winners=args.number_of_winners)

# data_reader.py --file_format=csv --file_name=participants1.csv --number_of_winners=2
