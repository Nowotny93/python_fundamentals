string = input()

output_list = []
data = ''
unique_symbols_count = 0

for ch in string:
    if not ch.isdigit():
        big_ch = ch.upper()
        output_list_joined = "".join(output_list)
        if big_ch not in output_list_joined and big_ch not in data:
            unique_symbols_count += 1
        data += big_ch
    elif ch.isdigit():
        multiplied_data = data * int(ch)
        output_list.append(multiplied_data)
        data = ''

print(f'Unique symbols used: {unique_symbols_count}')
print(f'{"".join(output_list)}')