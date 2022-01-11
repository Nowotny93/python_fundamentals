pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health_capacity = int(input())
command = input()

while command != "Retire":
    data = command.split()
    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                exit()
    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    exit()
    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health >= max_health_capacity:
                pirate_ship[index] = max_health_capacity
            else:
                pirate_ship[index] += health
    elif data[0] == "Status":
        treshold = max_health_capacity * 0.2
        counter = 0
        for section in pirate_ship:
            if section < treshold:
                counter += 1
        print(f"{counter} sections need repair.")
    command = input()

print(f'Pirate ship status: {sum(pirate_ship)}')
print(f'Warship status: {sum(warship)}')