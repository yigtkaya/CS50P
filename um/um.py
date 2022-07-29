import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    count = len(re.findall(r'\b'+ "um" + r'\b', s, re.IGNORECASE))
    return count

if __name__ == "__main__":
    main()