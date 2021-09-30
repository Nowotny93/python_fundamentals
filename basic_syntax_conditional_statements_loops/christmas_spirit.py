quantity = int(input())
days = int(input())

ornament_set = 0
tree_skirt = 0
tree_garlands = 0
tree_lights = 0
christamas_spirit = 0
counter = 0

while counter < days:
    counter += 1
    if counter % 11 == 0:
        quantity += 2
    if counter % 2 == 0:
        ornament_set += 2 * quantity
        christamas_spirit += 5
    if counter % 3 == 0:
        tree_skirt += 5 * quantity
        tree_garlands += 3 * quantity
        christamas_spirit += 13
    if counter % 5 == 0:
        tree_lights += 15 * quantity
        christamas_spirit += 17
        if counter % 3 == 0:
            christamas_spirit += 30
    if counter % 10 == 0:
        christamas_spirit -= 20
        tree_skirt += 5
        tree_garlands += 3
        tree_lights += 15
        if counter == days:
            christamas_spirit -= 30

total_cost = ornament_set + tree_garlands + tree_skirt + tree_lights
print(f'Total cost: {total_cost}')
print(f'Total spirit: {christamas_spirit}')