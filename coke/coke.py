due = 50

while True:
    print(f"Amouny Due: {due}")
    payed = int(input("Insert Coin: ").strip())

    if payed == due:
        owe = payed - due
        print(f"Change Owed: {owe}")
        break
    if payed == 25 or payed == 5 or payed == 10:
        due -= payed
        if due <= 0:
            print(f"Change Owed: {abs(due)}")
            break

