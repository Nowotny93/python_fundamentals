string = input().split('>')

output = ''
initial_strength = 0

for el in string:
    if not el[0].isdigit():
        output += el + '>'
    else:
        strenght = int(el[0])
        total_strength = initial_strength + strenght
        if len(el) == total_strength:
            output += '>'
        elif len(el) > total_strength:
            el_list = [str(x) for x in el]
            for i in range (0, total_strength):
                el_list[i] = 0
            final_list = [str(x) for x in el_list if x != 0]
            final_list_joined = ''.join(final_list)
            output += final_list_joined + '>'
        elif len(el) < total_strength:
            output += '>'
            initial_strength = 0
            initial_strength += total_strength - len(el)

final_output = output[:-1]
print(final_output)