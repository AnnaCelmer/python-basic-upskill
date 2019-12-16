from pathlib import Path

from data_reader import DataReader

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR.joinpath('data/lottery_templates')


class Prize:
    """
    Object of class Prize should contains data about a prize loaded from file.
    """
    def __init__(self, lottery_template):
        self.lottery_template = lottery_template

    def load_prize_data(self):
        lottery_template = DataReader.read_json_file(file_name=f'{TEMPLATES_DIR}/{self.lottery_template}.json')
        return lottery_template['prizes']
