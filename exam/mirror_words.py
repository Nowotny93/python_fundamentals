import re

text = input()

pattern = r'#[a-zA-Z]{3,}##[a-zA-Z]{3,}#|@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@'
matches = re.findall(pattern, text)

valid_matches = []
count = 0
for match in matches:
    count += 1
    if match[0] == '#':
        match_splt = match.split('##')
        first_word = match_splt[0]
        second_word = "".join(reversed(match_splt[1]))
        if first_word == second_word:
            match = ("".join(match)).replace('##', " <=> ")
            match = ("".join(match)).replace('#', "")
            valid_matches.append(match)
    elif match[0] == '@':
        match_splt = match.split('@@')
        first_word = match_splt[0]
        second_word = "".join(reversed(match_splt[1]))
        if first_word == second_word:
            match = ("".join(match)).replace('@@', " <=> ")
            match = ("".join(match)).replace('@', "")
            valid_matches.append(match)

if len(matches) == 0:
    print('No word pairs found!')
if count != 0:
    print(f'{count} word pairs found!')
if len(valid_matches) == 0:
    print('No mirror words!')
if len(valid_matches) != 0:
    print('The mirror words are:')
    print(", ".join(valid_matches))