from math import floor
import sys

def main():

    frac = input("Fraction: ").strip()
    print(gauge(convert(frac)))


def convert(fraction):
    x, y = fraction.split("/")
    if x.isdigit() and y.isdigit:
        x = int(x)
        y = int(y)
        percentage = (x / y) * 100
        return int(percentage)
    if y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError

def gauge(fuel):
    if fuel <= 1:
        return "E"
    elif fuel >= 99:
        return "F"
    else:
        return f"{fuel}%"
if __name__ == "__main__":
    main()