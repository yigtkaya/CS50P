grocery_list = []

while True:
    try:
        item = input().strip()
        grocery_list.append(item)
    except EOFError:

        grocery_set = sorted(set(grocery_list))

        for item in grocery_set:
            print(f"{grocery_list.count(item)} {item.upper()}")
        break


