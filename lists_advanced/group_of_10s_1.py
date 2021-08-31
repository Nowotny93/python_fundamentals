import math

numbers = [int(x) for x in input().split(', ')]

max_number = max(numbers)
number_of_groups = math.ceil(max_number / 10) * 10
random_list = []

for i in range (10, number_of_groups + 1, 10):
    for number in numbers:
        if int(number) <= i and int(number) != 0:
            random_list.append(number)
            index = numbers.index(number)
            numbers[index] = 0
    print(f"Group of {i}'s: {random_list}")
    random_list.clear()