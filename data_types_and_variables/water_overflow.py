number_of_lines = int(input())

amount = 0

for i in range (1, number_of_lines + 1):
    liters_of_water = int(input())
    amount += liters_of_water
    if amount > 255:
        print(f'Insufficient capacity!')
        amount -= liters_of_water

print(amount)