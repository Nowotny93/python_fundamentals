import re

str = input().lower()
magic_word = input().lower()

x = len(re.findall(rf"\b{magic_word}\b", str))

print(x)