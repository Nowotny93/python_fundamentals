import re

pattern = r"\b_[a-zA-Z]+\b"

text = input()
matches = re.findall(pattern, text)
matches_joined = ",".join(matches)
print(matches_joined.replace('_', ""))