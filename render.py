import sys

for line in sys.stdin:
    out = ""
    for ch in line.rstrip("\n"):
        if ch == " ":
            out += "\x1b[42m \x1b[0m"
        else:
            out += "\x1b[41m \x1b[0m"
    print(out)
