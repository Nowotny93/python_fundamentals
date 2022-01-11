def is_index_valid(collection: list, index):
    if 0 <= int(index) < len(collection):
        return True
    return False

def drop_func(collection: list, position):
    if is_index_valid(collection, position):
        item = collection.pop(int(position))
        collection.append(item)
    return collection

def steal_func(collection: list, count):
    stolen_items = []
    counter = 0
    if int(count) > len(collection):
        stolen_items += collection
    else:
        while counter < int(count):
            counter += 1
            item = collection.pop(-1)
            stolen_items.insert(0, item)
    print(", ".join(stolen_items))
    return collection

initial_loot = input().split('|')
command = input()

while command != "Yohoho!":
    splitted_command = command.split()
    cmd_type = splitted_command[0]
    cmd_index = splitted_command[1]
    if cmd_type == "Loot":
        splitted_command.remove(splitted_command[0])
        for i in splitted_command:
            if i not in initial_loot:
                initial_loot.insert(0, i)
    elif cmd_type == "Drop":
        initial_loot = drop_func(initial_loot, cmd_index)
    elif cmd_type == "Steal":
        initial_loot = steal_func(initial_loot, cmd_index)
    command = input()

if len(initial_loot) != 0:
    count_of_items_initial_loot = len(initial_loot)
    initial_loot_joined = "".join(initial_loot)
    sum_of_all_items_lenght = len(initial_loot_joined)
    average_treasure_gain = sum_of_all_items_lenght / count_of_items_initial_loot
    print(f'Average treasure gain: {average_treasure_gain:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')