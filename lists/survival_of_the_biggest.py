string = input()
n = int(input())

my_list = string.split()
result = []

for i in range(0, len(my_list)):
    number = int(my_list[i])
    result.append(number)

for z in range(0, n):
    min_number = min(result)
    result.remove(min_number)

result_str = str(result)[1:-1]
print(result_str)