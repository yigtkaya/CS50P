def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and greeting != "hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()



