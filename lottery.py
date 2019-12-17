import click
from pathlib import Path

import numpy as np

from data_reader import DataReader
from participants import Participants
from prize import Prize

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / 'data' / 'results'
TEMPLATES_DIR = BASE_DIR.joinpath('data/lottery_templates')


class Lottery:
    """Object of lottery class should contains number of participants,
     list of prizes and is able to do a lottery and produce results"""

    def __init__(self, file_name, lottery_template=None, output_file="result.json"):
        self.lottery_template = lottery_template
        self.output_file = output_file
        self.participants = Participants.read_data_from_file(file_name)
        self.prizes = Prize.load_prize_data()
        click.echo(f'Lottery template: {self.lottery_template}')

    def select_winners(self, number_of_winners):
        weights = self.verify_list_of_weights()
        return list(np.random.choice(self.participants, number_of_winners, replace=False, p=weights))

    def verify_list_of_weights(self):
        list_of_weights = [float(participant['weight']) if 'weight' in participant else 1.0 for participant in
                           self.participants]
        weights = np.array(list_of_weights)
        weights /= weights.sum()
        return weights

    def save_winners_data_to_json_file(self, data):
        DataReader.save_data_to_json_file(data, file_name=f'{RESULTS_DIR}/{self.output_file}')

    def award_prizes(self):
        for prize in self.prizes:
            prize['winners'] = self.select_winners(number_of_winners=prize['amount'])
            self.save_winners_data_to_json_file(self.prizes)
            for winner in prize['winners']:
                click.echo(click.style(
                    f"{winner['first_name']} {winner['last_name']} receives {prize['name']}",
                    fg='blue'))


@click.command()
@click.option('--file_name', help='File name with formatter included')  # todo: dodac param required
@click.option('--lottery_template', help='Lottery template name')
@click.option('--output_file', default='result.json', help='Output file name (only json format is supported)')
def main(file_name, lottery_template, output_file):
    lottery_template_1 = Lottery(file_name, lottery_template, output_file)
    lottery_template_1.award_prizes()
    # todo: dodac formatter - default json


if __name__ == '__main__':
    main()

# python3 lottery.py --file_name "participants1.csv" --lottery_template item_giveaway --output_file result_s.json
# python3 lottery.py --file_name "participants1.json" --lottery_template item_giveaway
# python3 lottery.py --file_name "participants1.json"
# python3 lottery.py --file_name "participants1.csv" --lottery_template separate_prizes
# python3 lottery.py --file_name "participants2" --lottery_template separate_prizes
