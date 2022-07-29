import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as f:
            lines = 0
            for line in f:
                text = line.strip()
                if not text.startswith("# ") and text != "":
                    lines += 1
        print(lines)
    except:
        sys.exit("File does not exist")