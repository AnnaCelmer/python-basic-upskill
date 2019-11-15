import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file_format', type=str, help='File format (csv or json)')
parser.add_argument('--file_name', type=str, help='File name')
parser.add_argument('--number_of_winners', type=int, help='Number of winners')

args = parser.parse_args()

print(args)
