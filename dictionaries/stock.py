data = input().split()
products = input().split()

dictionary = {}

for i in range (0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    dictionary[key] = int(value)

for el in products:
    if el in dictionary.keys():
        print(f'We have {dictionary[el]} of {el} left')
    else:
        print(f"Sorry, we don't have {el}")