x, y, z = input("Expression: ").split()

x, z = float(x), float(z)

if y == "+":
    print(x + z)
elif y == "/":
    print(x / z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)