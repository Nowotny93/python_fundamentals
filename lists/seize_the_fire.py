string = input().split('#')
water = int(input())

effort = 0
total_fire = 0
print('Cells:')

for info in string:
    separated_info = info.split(' = ')
    type_fire = separated_info[0]
    range = int(separated_info[1])

    if type_fire == "High" and 81 <= range <= 125 and water >= range:
        print(f' - {range}')
        effort += round((0.25 * range), 2)
        total_fire += range
        water -= range
    elif type_fire == "Medium" and 51 <= range <= 80 and water >= range:
        print(f' - {range}')
        effort += round((0.25 * range), 2)
        total_fire += range
        water -= range
    elif  type_fire == "Low" and 1 <= range <= 50 and water >= range:
        print(f' - {range}')
        effort += round((0.25 * range), 2)
        total_fire += range
        water -= range

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
