from pyfiglet import Figlet
import sys
try:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = Figlet(font=sys.argv[2])
        print(f.renderText(input("Input:")))
    else:
        sys.exit(1)
except:
    print("Invalid usage")
    sys.exit(1)