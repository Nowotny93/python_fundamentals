string = input()

digits = ''
letters = ''
other_symbols = ''

for el in string:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        other_symbols += el

print(digits)
print(letters)
print(other_symbols)