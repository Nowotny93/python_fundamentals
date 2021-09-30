budget = float(input())
price_kg_flour = float(input())

pack_of_eggs = price_kg_flour * 0.75
price_of_liter_milk = price_kg_flour + price_kg_flour * 0.25
price_of_quarter_milk = price_of_liter_milk / 4

total_price_of_cozonac = price_kg_flour + pack_of_eggs + price_of_quarter_milk
number_of_cozonacs = 0
number_of_eggs = 0

while budget >= total_price_of_cozonac:
    number_of_cozonacs += 1
    number_of_eggs += 3
    budget -= total_price_of_cozonac
    if number_of_cozonacs % 3 == 0:
        number_of_eggs -= number_of_cozonacs - 2

print(f"You made {number_of_cozonacs} cozonacs! Now you have {number_of_eggs} eggs and {budget:.2f}BGN left.")