from pathlib import Path

from data_reader import read_json_file

TEMPLATES_DIR = Path.cwd() / 'data' / 'lottery_templates'


class Prizes:

    def __init__(self, lottery_template):
        self.lottery_template = lottery_template
        self.list_of_prizes = []

    def load_prize_data(self):
        lottery_template = read_json_file(file_name=f'{TEMPLATES_DIR}/{self.lottery_template}.json')
        self.list_of_prizes = lottery_template['prizes']
