number_of_rows = int(input())

dictionary = {}

for i in range (1, number_of_rows + 1):
    name = input()
    grade = float(input())
    if name not in dictionary:
        dictionary[name] = grade
    else:
        dictionary[name] += grade
        dictionary[name] = dictionary[name] / 2

reversed_dict = dict(sorted(dictionary.items(), key = lambda x: -x[1]))
for (key, value) in reversed_dict.items():
    if value >= 4.50:
        print(f'{key} -> {value:.2f}')