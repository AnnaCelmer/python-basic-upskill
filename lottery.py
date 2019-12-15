import random
from pathlib import Path

from data_reader import DataReader
from participant import Participant
from prize import Prize

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR.joinpath('data/results')


class Lottery(Participant, Prize):
    """Object of lottery class should contains number of participants,
     list of prizes and is able to do a lottery and produce results"""

    def __init__(self, file_name, lottery_template, output_file="result.json"):
        Participant.__init__(self, file_name, file_format=file_name.split(".")[-1])
        Prize.__init__(self, lottery_template)
        self.lottery_template = lottery_template
        self.output_file = output_file
        self.participants = Participant.read_data_from_file(self)
        self.prizes = Prize.load_prize_data(self)

    def select_winners(self, number_of_winners):
        winners = random.sample(self.participants, number_of_winners)
        return winners

    def save_winners_data_to_json_file(self, data):
        DataReader.save_data_to_json_file(data, file_name=f'{RESULTS_DIR}/{self.output_file}')

    def award_prizes(self):
        for prize in self.prizes:
            prize['winners'] = self.select_winners(number_of_winners=prize['amount'])
            self.save_winners_data_to_json_file(self.prizes)


if __name__ == '__main__':
    lottery_template_1 = Lottery(file_name="participants1.csv", lottery_template="item_giveaway")
    lottery_template_1.award_prizes()
    lottery_template_2 = Lottery(file_name="participants1.json", lottery_template="separate_prizes",
                                 output_file="result_json.json")
    lottery_template_2.award_prizes()
    # lottery.award_prizes(file_format="json", file_name="participants1", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="json", file_name="participants2", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="json", file_name="participants2", lottery_template_name="separate_prizes")
    # lottery.award_prizes(file_format="csv", file_name="participants1", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="csv", file_name="participants1", lottery_template_name="separate_prizes")
    # lottery.award_prizes(file_format="csv", file_name="participants2", lottery_template_name="item_giveaway")
    # lottery.award_prizes(file_format="csv", file_name="participants2", lottery_template_name="separate_prizes")
