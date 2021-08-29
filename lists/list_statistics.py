lines = int(input())

positive_numbers = []
counte_of_positives = 0
negative_numbers = []
sum_of_negatives = 0

for i in range (1, lines + 1):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
        counte_of_positives += 1
    else:
        negative_numbers.append(number)
        sum_of_negatives += number

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {counte_of_positives}. Sum of negatives: {sum_of_negatives}')