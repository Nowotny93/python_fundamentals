import math

string = input().split()

dictionary = {}
number = ''
int_number = 0

for element in string:
    number = ''
    int_number = 0
    for ch in element:
        if ch.isdigit():
            number += ch
    for ch in element:
        if ch.isalpha() and ch == element[0]:
            if ch.islower():
                number_pos = ord(ch) - 96
                int_number += number_pos * int(number)
            elif ch.isupper():
                number_pos = ord(ch) - 64
                int_number += int(number) / number_pos
        elif ch.isalpha() and ch == element[-1]:
            if ch.islower():
                number_pos = ord(ch) - 96
                int_number += number_pos
            elif ch.isupper():
                number_pos = ord(ch) - 64
                int_number -= number_pos
    dictionary[element] = int_number

final_output = 0
for (key, value) in dictionary.items():
    final_output += value

rounded_output = round(final_output, 2)
print(f'{rounded_output:.2f}')