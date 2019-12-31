from pathlib import Path

import click

from lottery import Lottery
from participants import Participants
from prizes import Prizes

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
    participants.read_data_from_file(file_name, file_format)
    prizes = Prizes(specify_lottery_template(lottery_template))
    prizes.load_prize_data()
    lottery = Lottery(prizes, participants)
    lottery.award_prizes()
    lottery.save_awarded_prizes_data_to_json_file(output_file)


if __name__ == '__main__':
    main()
