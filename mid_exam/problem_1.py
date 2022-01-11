import math

budget = float(input())
students = int(input())
price_flour_package = float(input())
price_single_egg = float(input())
price_single_apron = float(input())

total_costs = 0

add_apron = math.ceil(students * 0.2 + students)
money_for_apron = price_single_apron * add_apron
total_costs += money_for_apron
money_for_eggs = price_single_egg * 10 * students
total_costs += money_for_eggs

for student in range (1, students + 1):
    if student % 5 == 0:
        money_for_flour = price_flour_package - price_flour_package
        total_costs += money_for_flour
    else:
        money_for_flour = price_flour_package
        total_costs += money_for_flour

if total_costs <= budget:
    print(f'Items purchased for {total_costs:.2f}$.')
else:
    needed_money = total_costs - budget
    print(f'{needed_money:.2f}$ more needed.')