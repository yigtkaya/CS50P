from math import floor
def main():
    percentage = 100 * fraction()

    if percentage < 1:
        print("E")
    elif percentage > 99:
        print('F')
    else:
        print(f"{floor(percentage)}%")

def fraction():

    while True:

        try:
            fractions = input("Fraction: ").strip().split("/")
            Y = int(fractions[1].replace("/", ""))
            X = int(fractions[0])

            if X <= Y:
                return X / Y
            else:
                print("Invalid input")

        except:
            print("Invalid input")

main()