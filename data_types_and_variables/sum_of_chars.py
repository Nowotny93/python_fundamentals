number_of_lines = int(input())

sum = 0

for i in range (1, number_of_lines + 1):
    symbol_as_int = input()
    symbol_into_ascii = ord(symbol_as_int)
    sum += symbol_into_ascii

print(f'The sum equals: {sum}')