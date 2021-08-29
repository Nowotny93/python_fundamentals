string = input()

my_list = string.split(",")

result = []
counter = 0

for i in range(0, len(my_list)):
    number = int(my_list[i])
    result.append(number)
    if number == 0:
        result.remove(number)
        counter += 1

for m in range (0, counter):
    result.append(0)

print(result)