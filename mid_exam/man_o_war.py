import sys

def is_index_valid(collection: list, index: int):
    if 0 <= index < len(collection):
        return True
    return False

def fire_func(collection: list, index: int, damage: int):
    if is_index_valid(collection, index):
        collection[index] -= damage
        if collection[index] <= 0:
            print('You won! The enemy ship has sunken.')
            sys.exit()
    return collection

def defend_func(collection: list, start_index: int, end_index: int, damage: int):
    if is_index_valid(collection, start_index):
        if is_index_valid(collection, end_index):
            for index in range(start_index, end_index + 1):
                collection[index] -= damage
                if collection[index] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    sys.exit()
    return collection

def repair_func(collection: list, index: int, health: int, maximum_health: int):
    if is_index_valid(collection, index):
        if maximum_health >= health:
            collection[index] += health
        else:
            collection[index] += maximum_health
    return collection

def status_func(collection: list, maximum_health: int):
    adjusted_maximum_health = maximum_health * 0.2
    count = 0
    for section in collection:
        if section < adjusted_maximum_health:
            count += 1
    print(f"{count} sections need repair.")
    return collection

status_pirate_ship = [int(x) for x in input().split('>')]
status_warship = [int(x) for x in input().split('>')]
max_health = int(input())
command = input()

while command != "Retire":
    command_splitted = command.split(' ')
    cmd_type = command_splitted[0]
    if cmd_type == "Fire":
        cmd_index = int(command_splitted[1])
        cmd_damage = int(command_splitted[2])
        status_warship = fire_func(status_warship, cmd_index, cmd_damage)
    elif cmd_type == "Defend":
        cmd_start_index = int(command_splitted[1])
        cmd_end_index = int(command_splitted[2])
        cmd_damage = int(command_splitted[3])
        status_pirate_ship = defend_func(status_pirate_ship, cmd_start_index, cmd_end_index, cmd_damage)
    elif cmd_type == "Repair":
        cmd_index = int(command_splitted[1])
        cmd_health = int(command_splitted[2])
        status_pirate_ship = repair_func(status_pirate_ship, cmd_index, cmd_health, max_health)
    elif cmd_type == "Status":
        status_pirate_ship = status_func(status_pirate_ship, max_health)
    command = input()

print(f'Pirate ship status: {sum(status_pirate_ship)}')
print(f'Warship status: {sum(status_warship)}')