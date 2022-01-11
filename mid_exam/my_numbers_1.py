numbers = [int(x) for x in input().split()]

average_value = round(sum(numbers) / len(numbers), 2)
top_five = sorted([x for x in numbers if x > average_value], reverse=True)

while len(top_five) > 5:
    top_five.pop(-1)

top_five_str = [str(x) for x in top_five]

if len(top_five_str) == 0:
    print('No')
else:
    print(f'{" ".join(top_five_str)}')