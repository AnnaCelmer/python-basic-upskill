from pathlib import Path

import click
import numpy as np

from data_reader import save_data_to_json_file

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / 'data' / 'results'
TEMPLATES_DIR = BASE_DIR / 'data' / 'lottery_templates'


class Lottery:
    """Object of lottery class should contains number of participants,
     list of prizes and is able to do a lottery and produce results"""

    def __init__(self, participants, prizes, lottery_template=None, output_file="result.json"):
        self.participants = participants
        self.lottery_template = lottery_template
        self.prizes = prizes
        self.output_file = output_file

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
        save_data_to_json_file(data, file_name=f'{RESULTS_DIR}/{self.output_file}')

    def award_prizes(self):
        for prize in self.prizes:
            prize['winners'] = self.select_winners(number_of_winners=prize['amount'])
            self.save_winners_data_to_json_file(self.prizes)
            for winner in prize['winners']:
                click.echo(click.style(
                    f"{winner['first_name']} {winner['last_name']} receives {prize['name']}",
                    fg='blue'))
