numbers = [int(x) for x in input().split()]
command = input()

while command != "Finish":
    command_splt = command.split()
    cmd_type = command_splt[0]
    cmd_value = int(command_splt[1])
    if cmd_type == "Add":
        numbers.append(cmd_value)
    elif cmd_type == "Remove":
        if cmd_value in numbers:
            numbers.remove(cmd_value)
    elif cmd_type == "Replace":
        cmd_new_value = int(command_splt[2])
        if cmd_value in numbers:
            needed_index = numbers.index(cmd_value)
            numbers.pop(needed_index)
            numbers.insert(needed_index, cmd_new_value)
    elif cmd_type == "Collapse":
        numbers = [x for x in numbers if x >= cmd_value]
        #for i in numbers:
            #if i < cmd_value:
                #numbers.remove(i)
    command = input()

numbers_str = [str(x) for x in numbers]
print(" ".join(numbers_str))