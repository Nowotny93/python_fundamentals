all_stops = list(input())
command = input()

while command != "Travel":
    command_splt = command.split(':')
    if command_splt[0] == "Add Stop":
        index = int(command_splt[1])
        string = command_splt[2]
        if 0 <= index < len(all_stops):
            all_stops.insert(index, string)
            all_stops = "".join(all_stops)
        print(all_stops)
    elif command_splt[0] == "Remove Stop":
        all_stops = list(all_stops)
        start_index = int(command_splt[1])
        end_index = int(command_splt[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            for i in range(start_index, end_index + 1):
                all_stops.pop(i)
                all_stops.insert(i, 0)
        all_stops = [str(x) for x in all_stops if x != 0]
        print("".join(all_stops))
    elif command_splt[0] == "Switch":
        all_stops = "".join(all_stops)
        all_stops = all_stops.replace('-', '::')
        all_stops = all_stops.split('::')
        old_string = command_splt[1]
        new_string = command_splt[2]
        for el in all_stops:
            if el == old_string:
                index = el.index(el)
                all_stops.pop(index)
                all_stops.insert(index, new_string)
        all_stops.insert(1, '::')
        all_stops.insert(-1, '-')
        print("".join(all_stops))
    command = input()

print(f'Ready for world tour! Planned stops: {"".join(all_stops)}')