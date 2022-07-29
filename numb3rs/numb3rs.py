import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    general_address = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    if general_address.match(ip):
        ports = ip.split(".")

        for port in ports:
            if int(port) > 255 or int(port) < 0:
                return False

        return True

    else:
        return False


if __name__ == "__main__":
    main()