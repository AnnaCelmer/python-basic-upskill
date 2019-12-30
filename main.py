from pathlib import Path

import click

from lottery import Lottery
from participants import Participants
from prize import Prize

TEMPLATES_DIR = Path.cwd() / 'data' / 'lottery_templates'


def specify_lottery_template(lottery_template):
    if lottery_template is None:
        lottery_template = next((e for e in TEMPLATES_DIR.iterdir() if e.is_file()), "No file with lottery template")
        return lottery_template.stem
    return lottery_template


@click.command()
@click.option('--file_name', help='File name with formatter included')
@click.option('--file_format', default='json', help='File name with formatter included')
@click.option('--lottery_template', help='Lottery template name')
@click.option('--output_file', default='result.json', help='Output file name (only json format is supported)')
def main(file_name, file_format, lottery_template, output_file):
    participants = Participants()
    list_of_participants = participants.read_data_from_file(file_name, file_format)
    prize = Prize()
    list_of_prizes = prize.load_prize_data(specify_lottery_template(lottery_template))
    lottery = Lottery()
    lottery.award_prizes(list_of_prizes, list_of_participants, output_file)


if __name__ == '__main__':
    main()

# python3 lottery.py --file_name "participants1.csv" --file_format "csv" --lottery_template item_giveaway --output_file result_s.json
# python3 lottery.py --file_name "participants1.json" --lottery_template item_giveaway
# python3 lottery.py --file_name "participants1.json"
# python3 lottery.py --file_name "participants1.csv" --lottery_template separate_prizes
# python3 lottery.py --file_name "participants2" --lottery_template separate_prizes
