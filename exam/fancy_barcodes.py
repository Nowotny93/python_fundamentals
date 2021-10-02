import re

count = int(input())

pattern = r'@#{1,}[A-Z][a-zA-Z0-9]{4,}[A-Z]@#{1,}'

for i in range (1, count + 1):
    random_string = input()
    match_or_not = re.match(pattern, random_string)
    if not match_or_not:
        print(f'Invalid barcode')
    else:
        product_group = ''
        for el in random_string:
            if el.isdigit():
                product_group += el
        if len(product_group) == 0:
            print(f'Product group: 00')
        else:
            print(f'Product group: {product_group}')