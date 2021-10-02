import re
import math

text = input()

pattern = r'[#|\|](?P<item>[A-Za-z ]+)[#|\|](?P<date>\d{2}/\d{2}/\d{2})[#|\|](?P<calories>\d+)[#|\|]'

matches = re.finditer(pattern, text)
total_calories = 0

for match in matches:
    total_calories += int(match.group('calories'))

days = math.floor(total_calories / 2000)
print(f'You have food to last you for: {days} days!')

matches = re.finditer(pattern, text)
for match in matches:
    print(f"Item: {match.group('item')}, Best before: {match.group('date')}, Nutrition: {match.group('calories')}")