import click


@click.option('--file_format', type=str, help='File format (csv or json)', default="json")
@click.option('--file_name', type=str, help='File name')
@click.option('--number_of_winners', type=int, help='Number of winners')
@click.option('--lottery_template', type=str, help='Chose the lottery template')
@click.option('--output_file', type=str, help='Output file with results')