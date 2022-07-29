import sys
from csv import DictReader
import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as f:
            menu = []
            reader = DictReader(f)
            for row in reader:
                menu.append(row)

            print(tabulate.tabulate(menu, headers="keys", tablefmt="grid"))
    except:
        sys.exit("File does not exist")