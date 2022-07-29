def main():

    s= convert(input("What time is it? ").replace(":", "."))
    
    if 7.0 <= s <= 8.0:
        print("breakfast time")
    elif 12.0 <= s <= 13.0:
        print("lunch time")
    elif 18.0 <= s <= 19.0:
        print("dinner time")

def convert(time):
    return float(time)


if __name__ == "__main__":
    main()