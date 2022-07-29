from random import randint

def main():
    question_count = 1
    tries = 0
    score = 0
    level = get_level()

    while question_count <=10:

        X = generate_integer(level)
        Y = generate_integer(level)

        while True:
            result = input(f"{X} + {Y} = ")
            try:
                if result.isdigit():
                    if int(result) == X+Y:
                        score +=1
                        break
                    else:
                        print("EEE")
                        tries +=1
                else:
                        print("EEE")
                        tries +=1
                if tries ==3:
                    print(f"{X} + {Y} = {X+Y}")
                    tries = 0
                    break
            except:
                continue
        question_count +=1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level >= 1 and level <=3:
                return level
            else:
                raise ValueError
        except:
            continue

def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)


if __name__ == "__main__":
    main()