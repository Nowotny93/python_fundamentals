import re

text = input()

pattern = r'=[A-Z][a-zA-Z][a-zA-Z]+=|/[A-Z][a-zA-Z][a-zA-Z]+/'

matches = re.findall(pattern, text)
final_list = []

for match in matches:
    if '=' in match:
       match = match.replace('=', "")
       final_list.append(match)
    elif '/' in match:
        match = match.replace('/', "")
        final_list.append(match)

print(f'Destinations: {", ".join(final_list)}')
print(f'Travel Points: {len("".join(final_list))}')