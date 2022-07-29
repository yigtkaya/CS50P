import sys
from csv import DictReader, DictWriter

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1], "r") as before:
            reader = DictReader(before)

            with open(sys.argv[2], "w") as after:
                writer = DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    last_name, first_name = row["name"].split(", ")
                    house = row["house"]

                    writer.writerow(
                        {"first": first_name, "last": last_name, "house": house}
                    )
    except:
        sys.exit("File does not exist")