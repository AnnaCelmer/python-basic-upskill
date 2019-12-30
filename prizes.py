from pathlib import Path

from data_reader import read_json_file

TEMPLATES_DIR = Path.cwd() / 'data' / 'lottery_templates'


class Prizes:

    def __init__(self):
        self.list_of_prizes = []

    def load_prize_data(self, lottery_template):
        lottery_template = read_json_file(file_name=f'{TEMPLATES_DIR}/{lottery_template}.json')
        self.list_of_prizes = lottery_template['prizes']
        return self.list_of_prizes
