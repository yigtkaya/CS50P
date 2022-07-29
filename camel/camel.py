import re

ask = input("camelCase: ").strip()

a, b = re.split("[A-Z]", ask)

b = b.lower()

print(f"snake_case: {a}_{b}")
