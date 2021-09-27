resource = input()

dictionary = {}

while resource != "stop":
    quantity = int(input())
    if resource not in dictionary:
        dictionary[resource] = quantity
    else:
        dictionary[resource] += quantity
    resource = input()

for (key, value) in dictionary.items():
    print(f'{key} -> {value}')