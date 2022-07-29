def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    num = 0
    s_last = s[2:]
    not_allowed = [".", ",", ":", "*", "?"]
    if 2 <= len(s) <= 6:
        if s.isalpha():
            return True
        if s.isnumeric():
            return False

        if s[:2].isalpha():

            for char in s_last:
                if char in not_allowed:
                    return False
                else:
                    if char.isnumeric() and num == 0 and char == "0":
                        return False
                    elif char.isnumeric():
                        num +=1
                    elif char.isalpha() and num != 0:
                        return False
            return True
        else:
            return False
main()