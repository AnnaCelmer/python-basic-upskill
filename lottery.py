from pathlib import Path

import click
import numpy as np

from data_reader import save_data_to_json_file

RESULTS_DIR = Path.cwd() / 'data' / 'results'
TEMPLATES_DIR = Path.cwd() / 'data' / 'lottery_templates'


class Lottery:
    """Object of lottery class should contains number of participants,
     list of prizes and is able to do a lottery and produce results"""

    def select_winners(self, participants, number_of_winners):
        weights = self.verify_list_of_weights(participants)
        if number_of_winners > len(participants):
            number_of_winners = len(participants)
            click.echo(f"Number of winners ({number_of_winners}) is less than number of participants ({participants})")
        return list(np.random.choice(participants, number_of_winners, replace=False, p=weights))

    @staticmethod
    def verify_list_of_weights(participants):
        list_of_weights = [float(participant['weight']) if 'weight' in participant else 1.0 for participant in
                           participants]
        weights = np.array(list_of_weights)
        weights /= weights.sum()
        return weights

    @staticmethod
    def save_winners_data_to_json_file(data, output_file):
        save_data_to_json_file(data, file_name=f'{RESULTS_DIR}/{output_file}')

    def award_prizes(self, prizes, participants, output_file):
        for prize in prizes:
            prize['winners'] = self.select_winners(participants, number_of_winners=prize['amount'])
            self.save_winners_data_to_json_file(prizes, output_file)
            for winner in prize['winners']:
                click.echo(
                    click.style(f"{winner['first_name']} {winner['last_name']} receives {prize['name']}", fg='blue'))
                participants.remove(winner)
        return prizes
