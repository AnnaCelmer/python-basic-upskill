from pathlib import Path

import click
import numpy as np

from data_reader import save_data_to_json_file

RESULTS_DIR = Path.cwd() / 'data' / 'results'
TEMPLATES_DIR = Path.cwd() / 'data' / 'lottery_templates'


class Lottery:

    def __init__(self, prizes, participants):
        self.winners = []
        self.awarded_prizes = []
        self.list_of_prizes = prizes.list_of_prizes
        self.base_list_of_participants = participants.list_of_participants
        self.updated_list_of_participants = participants.list_of_participants

    def select_winners(self, number_of_winners):
        self.updated_list_of_participants = [participant for participant in self.base_list_of_participants if
                                             participant not in self.winners]
        weights = self.verify_list_of_weights()
        if number_of_winners > len(self.updated_list_of_participants):
            number_of_winners = len(self.updated_list_of_participants)
            click.echo(
                f"Number of winners ({number_of_winners}) is less than number of participants"
                f" ({self.updated_list_of_participants})")
        return list(np.random.choice(self.updated_list_of_participants, number_of_winners, replace=False, p=weights))

    def verify_list_of_weights(self):
        list_of_weights = [float(participant['weight']) if 'weight' in participant else 1.0 for participant in
                           self.updated_list_of_participants]
        weights = np.array(list_of_weights)
        weights /= weights.sum()
        return weights

    def save_awarded_prizes_data_to_json_file(self, output_file):
        save_data_to_json_file(self.awarded_prizes, file_name=f'{RESULTS_DIR}/{output_file}')

    def award_prizes(self):
        for prize in self.list_of_prizes:
            prize['winners'] = self.select_winners(number_of_winners=prize['amount'])
            self.awarded_prizes.append(prize)
            for winner in prize['winners']:
                self.winners.append(winner)
                click.echo(
                    click.style(f"{winner['first_name']} {winner['last_name']} receives {prize['name']}", fg='blue'))
