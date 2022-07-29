import re
import sys


def main():

    print(convert(input("Hours: ")))

def RepresentInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def convert(s):
    if "to" in s:
        shiftHours = s.split("to")
        start, end = shiftHours[0].strip(), shiftHours[1].strip()

        if " " not in start or " " not in end:
            raise ValueError
    else:
        raise ValueError

    start = start.split(" ")
    end = end.split(" ")

    if ":" in start[0]:
        start = start[0].split(":")
        start_minute = start[1]
        start_hour = start[0]
    else:
        start_hour = start[0]
        start_minute = "00"

    if ":" in end[0]:
        end = end[0].split(":")
        end_minute = end[1]
        end_hour = end[0]
    else:
        end_hour = end[0]
        end_minute = "00"



    if "AM" in shiftHours[0].strip():

        if int(start_hour) <= 12:
            if start_hour == "12":
                start_hour = "00"
        else:
            raise ValueError

        if RepresentInt(start_minute):
            if int(start_minute) >= 60:
                raise ValueError


    elif "PM" in shiftHours[0].strip():

        if end_hour == "0" or end_hour == "00":
            raise ValueError
        if int(start_hour) < 12:
            start_hour = int(start_hour) + 12

        if RepresentInt(start_minute):
            if int(start_minute) >= 60:
                raise ValueError

    else:
        raise ValueError

    if "AM" in shiftHours[1].strip():

        if int(end_hour) <= 12:
            if end_hour == "12":
                end_hour = "00"
        else:
            raise ValueError

        if RepresentInt(end_minute):
            if int(start_minute) >= 60:
                raise ValueError


    elif "PM" in shiftHours[1].strip():

        if end_hour == "0" or end_hour == "00":
            raise ValueError

        if int(end_hour) < 12:
            end_hour = int(end_hour) + 12


        if RepresentInt(end_minute):

            if int(start_minute) >= 60:
                raise ValueError

    else:
        raise ValueError

    return f"{str(start_hour).zfill(2)}:{start_minute.zfill(2)} to {str(end_hour).zfill(2)}:{end_minute.zfill(2)}"

if __name__ == "__main__":
    main()