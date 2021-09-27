command = input()

dictionary = {}
total_products = 0
total_quantity = 0

while command != "statistics":
    command_splt = command.split()
    key = command_splt[0]
    value = int(command_splt[1])
    total_quantity += value
    if key in dictionary.keys():
        dictionary[key] += value
    else:
        total_products += 1
        dictionary[key] = int(value)
    command = input()

print('Products in stock:')
for (product, quantity) in dictionary.items():
    print(f'- {product} {quantity}')
print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')