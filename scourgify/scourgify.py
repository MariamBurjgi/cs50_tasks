import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

try:
    with open(sys.argv[1], newline='') as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = ['first', 'last', 'house']
        with open(sys.argv[2], 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                name = row['name']
                last, first = name.split(', ')
                writer.writerow({'first': first, 'last': last, 'house': row['house']})
except FileNotFoundError:
    sys.exit("Error: input file not found")
