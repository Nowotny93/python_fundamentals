import re

text = input()

pattern = r'::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*'
cool_threshold = 0

for ch in text:
    if ch.isdigit():
        if cool_threshold == 0:
            cool_threshold = int(ch)
        else:
            cool_threshold *= int(ch)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(re.findall(pattern, text))} emojis found in the text. The cool ones are:')

matches = (re.findall(pattern, text))
ascii_sum_per_match = 0
for match in matches:
    for ch in match:
        if ch.isalpha():
            ascii_sum_per_match += ord(ch)
            if ascii_sum_per_match >= cool_threshold:
                print(match)
                ascii_sum_per_match = 0
                break