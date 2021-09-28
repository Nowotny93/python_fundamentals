key = int(input())
number_of_lines = int(input())

result_as_str = ''

for i in range (1, number_of_lines + 1):
    line = str(input())
    line_as_int = ord(line)
    end_line = line_as_int + key
    result = chr(end_line)
    result_as_str += str(result)

print(result_as_str)

