import random
import click
from pathlib import Path

from data_reader import DataReader

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR.joinpath('data/lottery_templates')
RESULTS_DIR = BASE_DIR.joinpath('data/results')


# @click.option('--file_format', type=str, help='File format (csv or json)', default="json")
# @click.option('--file_name', type=str, help='File name')
# @click.option('--number_of_winners', type=int, help='Number of winners')
# @click.option('--lottery_template', type=str, help='Chose the lottery template')
# @click.option('--output_file', type=str, help='Output file with results')
class Lottery(DataReader):
    def __init__(self):
        DataReader.__init__(self)

    def select_winners(self, file_format, file_name, number_of_winners):
        data = self.read_data_from_file(file_format, file_name)
        winners = random.sample(data, number_of_winners)
        return winners

    def select_lottery_template(self, lottery_template_name):
        return self.read_json_file(file_name=f'{TEMPLATES_DIR}/{lottery_template_name}.json')

    def award_prizes(self, file_format, file_name, lottery_template_name):
        lottery_template = self.select_lottery_template(lottery_template_name)
        for prize in lottery_template['prizes']:
            prize['winners'] = self.select_winners(file_format=file_format,
                                                   file_name=f'{BASE_DIR}/data/{file_name}.{file_format}',
                                                   number_of_winners=prize['amount'])
            print(f"{prize['name']} receives {prize['winners'][0]['first_name']} {prize['winners'][0]['last_name']}")
        self.save_data_to_json_file(lottery_template, file_name=f'{RESULTS_DIR}/result.json')


if __name__ == '__main__':
    lottery = Lottery()
    # lottery.award_prizes(file_format="json", file_name="participants1", lottery_template_name="item_giveaway")
    lottery.award_prizes(file_format="json", file_name="participants1", lottery_template_name="separate_prizes")
    # lottery.award_prizes(file_format="json", file_name="participants2", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="json", file_name="participants2", lottery_template_name="separate_prizes")
    # lottery.award_prizes(file_format="csv", file_name="participants1", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="csv", file_name="participants1", lottery_template_name="separate_prizes")
    # lottery.award_prizes(file_format="csv", file_name="participants2", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="csv", file_name="participants2", lottery_template_name="separate_prizes")