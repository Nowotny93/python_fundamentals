targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command_splt = command.split()
    cmd_type = command_splt[0]
    cmd_index = int(command_splt[1])
    cmd_value = int(command_splt[2])
    if cmd_type == "Shoot":
        if 0 <= cmd_index < len(targets):
            targets[cmd_index] -= cmd_value
            if targets[cmd_index] <= 0:
                targets.pop(cmd_index)
    elif cmd_type == "Add":
        if 0 <= cmd_index < len(targets):
            targets.insert(cmd_index, cmd_value)
        else:
            print('Invalid placement!')
    elif cmd_type == "Strike":
        left_strike_index = cmd_index - cmd_value
        right_strike_index = cmd_index + cmd_value
        if 0 <= left_strike_index < len(targets) and 0 <= cmd_index < len(targets) and 0 <= right_strike_index < len(targets):
            for i in range(left_strike_index, right_strike_index + 1):
                targets.pop(left_strike_index)
        else:
            print('Strike missed!')
    command = input()

targets_str = [str(x) for x in targets]
print("|".join(targets_str))