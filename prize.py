from pathlib import Path

from data_reader import read_json_file

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / 'data' / 'lottery_templates'


class Prize:
    """
    Object of class Prize should contains data about a prize loaded from file.
    """

    @staticmethod
    def load_prize_data(lottery_template):
        lottery_template = read_json_file(file_name=f'{TEMPLATES_DIR}/{lottery_template}.json')
        return lottery_template['prizes']
