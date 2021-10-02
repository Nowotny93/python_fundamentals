import re

pattern = r"(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)"
pattern_numbers = r"\d"
text = input()

all_numbers_in_text_as_strings = re.findall(pattern_numbers, text)
all_numbers_as_integers = [int(num_str) for num_str in all_numbers_in_text_as_strings]

threshold = 1
for num in all_numbers_as_integers:
    threshold *= num

emoji_matches = re.finditer(pattern, text)
print(f"Cool threshold: {threshold}")

emojis_to_print = []

emoji_count = 0
for match in emoji_matches:
    emoji_count += 1
    data = match.groupdict()
    emoji = data["emoji"]
    emoji_coolnes = sum([ord(letter) for letter in emoji])
    if emoji_coolnes >= threshold:
        emojis_to_print.append(f"{data['surr']}{data['emoji']}{data['surr']}")

print(f"{emoji_count} emojis found in the text. The cool ones are:")
# print("\n".join(emojis_to_print))
for emoji in emojis_to_print:
    print(emoji)