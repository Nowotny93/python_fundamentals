words = input().split()

dictionary = {}

for el in words:
    word_lower = el.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end = " ")

