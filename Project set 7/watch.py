import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches:=re.search(r"^(?:.+)(https?://)(?:www\.)?(youtube\.com)?/embed(/xvFZjo5PgG0)?(?:.+)$",s,re.IGNORECASE):
        us=re.sub(r"^(?:.+)youtube\.com(?:.+)$","youtu.be",s)
        if "https://"==matches.group(1):
            if matches.group(3)==None:
                return(matches.group(1)+us)
            else:
                return(matches.group(1)+us+matches.group(3))
        elif "http://"==matches.group(1):
            novo="https://"
            if matches.group(2)==None and matches.group(3)==None:

                return(novo+"youtu.be")
            elif matches.group(3)==None:
                novo="https://"
                return(novo+us)
            else:
                return(novo+us+matches.group(3))


if __name__ == "__main__":
    main()
