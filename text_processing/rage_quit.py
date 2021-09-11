import re

string = input()

output = ''
current_ouput = ''

string = [x for x in re.split('(-?\d+\.?\d*)', string) if x != '']

for char in string:
    big_ch = char.upper()
    if big_ch.isdigit():
        current_ouput = current_ouput * int(big_ch)
        output += current_ouput
        current_ouput = ''
    else:
        current_ouput+=big_ch

if len(output)==0:
    output = current_ouput

number_unique = len(set(output))
print(f'Unique symbols used:', number_unique)
print(output)