import re

def main():
    inn = input("Input: ").strip()
    print(f"Output: {shorten(inn)}")

def shorten(m):
    return re.sub("[aeiouAEIOU]", "", m)

if __name__ == "__main__":
    main()