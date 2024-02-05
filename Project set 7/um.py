import re
import sys

def main():
    print(count(input("Input: ")))

def count(s):
    p = len(re.findall(r"(?<![a-zA-Z])um(?![a-zA-Z])", s.lower(), re.IGNORECASE))
    return int(p)


if __name__ == "__main__":
    main()

