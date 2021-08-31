random_numbers = input().split(', ')

random_numbers_int = list(map(lambda x: int(x), random_numbers))
positive_numbers = [x for x in random_numbers_int if x>= 0]
positive_numbers_str = [str(x) for x in positive_numbers]
print(f'Positive: {", ".join(positive_numbers_str)}')
negative_numbers = [x for x in random_numbers_int if x < 0]
negative_numbers_str = [str(x) for x in negative_numbers]
print(f'Negative: {", ".join(negative_numbers_str)}')
even_numbers = [x for x in random_numbers_int if x % 2 == 0]
even_numbers_str = [str(x) for x in even_numbers]
print(f'Even: {", ".join(even_numbers_str)}')
odd_numbers = [x for x in random_numbers_int if x % 2 != 0]
odd_numbers_str = [str(x) for x in odd_numbers]
print(f'Odd: {", ".join(odd_numbers_str)}')