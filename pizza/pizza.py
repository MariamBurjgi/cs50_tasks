import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) > 2 or not sys.argv[1].endswith(".csv"):
        sys.exit(1)
    else:
        table = []
        with open(f"{sys.argv[1]}") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
except FileNotFoundError:
    sys.exit("File Not Found")
print(tabulate(table,headers="firstrow", tablefmt="grid"))