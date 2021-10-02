import re
import math

text = input()

pattern = r'\|[A-Za-z ]+\|\d{2}/\d{2}/\d{2}\|\d+\||#[A-Za-z ]+#\d{2}/\d{2}/\d{2}#\d+#'

matches = re.findall(pattern, text)
total_calories = 0

for match in matches:
    if '#' in match:
        match_splt = match.split('#')
        total_calories += int(match_splt[-2])
    elif '|' in match:
        match_splt_second = match.split('|')
        total_calories += int(match_splt_second[-2])

days = math.floor(total_calories / 2000)
print(f'You have food to last you for: {days} days!')

matches = re.findall(pattern, text)
for match in matches:
    if '#' in match:
        match_splt = match.split('#')
        print(f"Item: {match_splt[1]}, Best before: {match_splt[2]}, Nutrition: {match_splt[3]}")
    elif '|' in match:
        match_splt_second = match.split('|')
        print(f"Item: {match_splt_second[1]}, Best before: {match_splt_second[2]}, Nutrition: {match_splt_second[3]}")