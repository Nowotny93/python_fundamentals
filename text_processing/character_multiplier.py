string = input().split()

first_string = string[0]
second_string = string[1]
first_string_int = [ord(x) for x in first_string]
second_string_int = [ord(x) for x in second_string]

sum = 0

if len(string[0]) != len(string[1]):
    needed_str = abs(len(string[0]) - len(string[1]))

if len(string[0]) > len(string[1]):
    for i in range (1, needed_str + 1):
        second_string_int.append(1)
elif len(string[0]) < len(string[1]):
    for i in range (1, needed_str + 1):
        first_string_int.append(1)

for i in range (0, len(first_string_int)):
    sum += first_string_int[i] * second_string_int[i]

print(sum)