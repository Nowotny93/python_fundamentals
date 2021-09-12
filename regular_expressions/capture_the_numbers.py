import re

pattern = r"\d+"

while True:
    try:
        text = input()
        matches = re.findall(pattern, text)
        if len(matches) == 0:
            continue
        print(" ".join(matches), end=" ")
    except EOFError:
        break