numbers = [int(x) for x in input().split()]

average_value = round(sum(numbers) / len(numbers), 2)
greater_than_average = []

for number in numbers:
    if number > average_value:
        greater_than_average.append(number)

if len(greater_than_average) == 0:
    print('No')
elif len(greater_than_average) > 5:
    greater_than_average.sort(reverse=True)
    top_five_list = []
    for i in range(0, 5):
        top_five_list.append(greater_than_average[i])
    top_five_list_str = [str(x) for x in top_five_list]
    print(f'{" ".join(top_five_list_str)}')
elif len(greater_than_average) <= 5:
    greater_than_average.sort(reverse=True)
    greater_than_average_str = [str(x) for x in greater_than_average]
    print(f'{" ".join(greater_than_average_str)}')