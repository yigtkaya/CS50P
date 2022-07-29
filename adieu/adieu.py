import inflect
p = inflect.engine()
names =[]
while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
        to_string_names = p.join(names)
    except EOFError:
        print("Adieu, adieu, to " + to_string_names)
        break