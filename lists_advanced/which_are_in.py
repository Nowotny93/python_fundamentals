input_line_1 = input().split(", ")
input_line_2 = input().split(", ")

final_line = []

for el in input_line_1:
    for el_1 in input_line_2:
        if el in el_1:
            final_line.append(el)
            break

print(final_line)