from datetime import date
import inflect
import sys
p = inflect.engine()
def main():

    print(Age(input("Date Of Birth: ")))


def Age(s):
    try:
        born = s.split("-")
        birthDate = date(int(born[0]),int(born[1]),int(born[2]))
        today = date.today()

        time_diff = today - birthDate

        minutes_diff = time_diff.days * 24* 60
        minutes_diff = p.number_to_words(minutes_diff, andword="")

        minutes_diff += " minutes"
        return minutes_diff.capitalize()
    except ValueError:
        sys.exit(1)

if __name__ == "__main__":
    main()