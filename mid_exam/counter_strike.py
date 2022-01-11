initial_energy = int(input())
command = input()

won_battles = 0
energy_is_enough = True

while command != "End of battle":
    distance = int(command)
    if initial_energy >= distance:
        won_battles += 1
        initial_energy -= distance
        if won_battles % 3 == 0:
            initial_energy += won_battles
    else:
        energy_is_enough = False
        break
    command = input()

if energy_is_enough:
    print(f'Won battles: {won_battles}. Energy left: {initial_energy}')
else:
    print(f'Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy')