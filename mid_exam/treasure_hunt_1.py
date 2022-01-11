initial_treasure = input().split("|")
command = input()

while command != "Yohoho!":
    command_splt = command.split()
    cmd_type = command_splt[0]
    if cmd_type == "Loot":
        command_splt.remove(cmd_type)
        for item in command_splt:
            if item not in initial_treasure:
                initial_treasure.insert(0, item)
    elif cmd_type == "Drop":
        index = int(command_splt[1])
        if 0 <= index < len(initial_treasure):
            element = initial_treasure.pop(index)
            initial_treasure.append(element)
    elif cmd_type == "Steal":
        count = int(command_splt[1])
        if len(initial_treasure) <= count:
            print(", ".join(initial_treasure))
            initial_treasure.clear()
        else:
            stolen_items = []
            end_count = len(initial_treasure) - count
            for el_index in range (len(initial_treasure)-1, end_count -1, -1):
                stolen_items.append(initial_treasure[el_index])
                initial_treasure.remove(initial_treasure[el_index])
            stolen_items.reverse()
            print(", ".join(stolen_items))
    command = input()

if len(initial_treasure) != 0:
    count_of_all_items = len(initial_treasure)
    final_treasure_concatenated = "".join(initial_treasure)
    sum_final_treasure_ch = len(final_treasure_concatenated)
    average_treasure_gain = sum_final_treasure_ch / count_of_all_items
    print(f'Average treasure gain: {average_treasure_gain:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
