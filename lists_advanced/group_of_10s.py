random_numbers = input().split(', ')

random_numbers_int = list(map(lambda x: int(x), random_numbers))
max_number = str(max(random_numbers_int))
max_number_splitted = [int(x) for x in max_number]
max_number_splitted_int = list(map(lambda x: int(x), max_number_splitted))

if max_number_splitted_int[1] != 0:
    max_number_splitted_int[0] += 1
    max_number_splitted_int[1] = 0

last_category_str = [str(x) for x in max_number_splitted_int]
last_category_joined = "".join(last_category_str)
numbers_under_tens = []

for tens in range(10, int(last_category_joined) + 10, 10):
    numbers_under_tens = [x for x in random_numbers_int if x <= tens]
    print(f"Group of {tens}'s: {numbers_under_tens}")
    for i in numbers_under_tens:
        random_numbers_int.remove(i)