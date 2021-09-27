command = input()

dictionary_quantity = {}
dictionary_price = {}

while command != 'buy':
    splt_command = command.split()
    product = splt_command[0]
    price = float(splt_command[1])
    quantity = int(splt_command[2])
    if product not in dictionary_quantity:
        dictionary_quantity[product] = quantity
    else:
        dictionary_quantity[product] += quantity
    if product not in dictionary_price:
        dictionary_price[product] = price
    else:
        dictionary_price[product] = price
    command = input()

final_dict = {}
for (keys, values) in dictionary_quantity.items():
    if keys in dictionary_price:
        final_dict[keys] = dictionary_quantity[keys] * dictionary_price[keys]

for (keys, values) in final_dict.items():
    print(f'{keys} -> {values:.2f}')