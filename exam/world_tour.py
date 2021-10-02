all_stops = input()
command = input()

while command != "Travel":
    command_splt = command.split(':')
    if command_splt[0] == "Add Stop":
        index = int(command_splt[1])
        string = command_splt[2]
        if 0 <= index < len(all_stops):
            all_stops = all_stops[:index] + string + all_stops[index:]
        print(all_stops)
    elif command_splt[0] == "Remove Stop":
        start_index = int(command_splt[1])
        end_index = int(command_splt[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
        print(all_stops)
    elif command_splt[0] == "Switch":
        old_string = command_splt[1]
        new_string = command_splt[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
        print(all_stops)
    command = input()

print(f'Ready for world tour! Planned stops: {all_stops}')