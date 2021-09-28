import math

quantity = int(input())
days = int(input())

counter = 0
total_coins = 0

while counter < days:
    counter += 1
    total_coins += 50 - 2 * quantity
    if counter % 10 == 0:
        quantity -= 2
    if counter % 15 == 0:
        quantity += 5
    if counter % 3 == 0:
        total_coins -= 3 * quantity
    if counter % 5 == 0:
        total_coins += 20 * quantity
        if counter % 3 == 0:
            total_coins -= 2 * quantity

average_coins = total_coins / quantity
print(f'{quantity} companions received {math.floor(average_coins)} coins each.')