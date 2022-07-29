import validators

def main():
    isValid(input("What's your email address?").strip())

def isValid(s):

    if validators.email(s):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()