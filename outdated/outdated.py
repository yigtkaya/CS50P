months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month , day, year = map(int, date.split("/"))
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        if "," in date:
            month, day, year = date.split("/")
            month = months.index(month) + 1
            day = int(day)
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

    except ValueError:
        continue
    except (EOFError, KeyboardInterrupt):
            print('', end='\n')
            quit()