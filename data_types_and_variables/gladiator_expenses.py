lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

counter = 0
counter_shield = 0
helmet_costs = 0
sword_costs = 0
shield_costs = 0
armor_costs = 0

while counter < lost_fights:
    counter += 1
    if counter % 2 == 0:
        helmet_costs += helmet_price
        if counter % 3 == 0:
            shield_costs += shield_price
            counter_shield += 1
            if counter_shield % 2 == 0:
                armor_costs += armor_price
    if counter % 3 == 0:
        sword_costs += sword_price

total_expenses = helmet_costs + sword_costs + shield_costs + armor_costs
print(f'Gladiator expenses: {total_expenses:.2f} aureus')

