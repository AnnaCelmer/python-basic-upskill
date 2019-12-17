import os
from os.path import isfile, join
from pathlib import Path

import click

from lottery import Lottery
from participants import Participants
from prize import Prize

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / 'data' / 'lottery_templates'


def specify_lottery_template(lottery_template):
    if lottery_template is None:
        lottery_template = next((f for f in os.listdir(TEMPLATES_DIR) if isfile(join(TEMPLATES_DIR, f))),
                                "No file with lottery template")
    return lottery_template.split(".")[0] if "." in lottery_template else lottery_template


@click.command()
@click.option('--file_name', help='File name with formatter included')  # todo: dodac param required
@click.option('--file_format', default='json', help='File name with formatter included')  # todo: dodac param required
@click.option('--lottery_template', help='Lottery template name')
@click.option('--output_file', default='result.json', help='Output file name (only json format is supported)')
def main(file_name, file_format, lottery_template, output_file):
    file_name = file_name if "." in file_name else f"{file_name}.{file_format}"
    participants = Participants()
    list_of_participants = participants.read_data_from_file(file_name, file_format)
    prize = Prize()
    list_of_prizes = prize.load_prize_data(specify_lottery_template(lottery_template))
    lottery = Lottery(list_of_participants, list_of_prizes, lottery_template, output_file)
    lottery.award_prizes()


if __name__ == '__main__':
    main()

# python3 lottery.py --file_name "participants1.csv" --file_format "csv" --lottery_template item_giveaway --output_file result_s.json
# python3 lottery.py --file_name "participants1.json" --lottery_template item_giveaway
# python3 lottery.py --file_name "participants1.json"
# python3 lottery.py --file_name "participants1.csv" --lottery_template separate_prizes
# python3 lottery.py --file_name "participants2" --lottery_template separate_prizes
