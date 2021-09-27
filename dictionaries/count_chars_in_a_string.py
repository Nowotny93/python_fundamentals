line = input()

dictionary = {}
value = 0

for ch in line:
    if ch == ' ':
        continue
    if ch not in dictionary:
        value += 1
        dictionary[ch] = int(value)
    else:
        dictionary[ch] += 1
    value = 0

for (key, value) in dictionary.items():
    print(f'{key} -> {value}')