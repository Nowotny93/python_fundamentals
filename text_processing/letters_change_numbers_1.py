string = input().split()

total_sum = 0
number = 0

for el in string:
    for i in el:
        if i.isalpha() and i == el[0]:
            number = int(el[1:-1])
            if i.islower():
                letter_pos = ord(i) - 96
                number = letter_pos * number
            elif i.isupper():
                letter_pos = ord(i) - 64
                number = number / letter_pos
        elif i.isalpha() and i == el[-1]:
            if i.islower():
                letter_pos = ord(i) - 96
                number += letter_pos
            elif i.isupper():
                letter_pos = ord(i) - 64
                number -= letter_pos
    total_sum += number
    number = 0

total_sum_round = round(total_sum, 2)
print(f'{total_sum_round:.2f}')