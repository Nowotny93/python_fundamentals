list = input().split("!")
command = input()

while command != "Go Shopping!":
    command_splitted = command.split()
    cmd_type = command_splitted[0]
    cmd_item = command_splitted[1]
    if cmd_type == "Urgent":
        if cmd_item not in list:
            list.insert(0, cmd_item)
    elif cmd_type == "Unnecessary":
        if cmd_item in list:
            list.remove(cmd_item)
    elif cmd_type == "Correct":
        cmd_new_item = command_splitted[2]
        if cmd_item in list:
            item = list.index(cmd_item)
            list.pop(item)
            list.insert(item, cmd_new_item)
    elif cmd_type == "Rearrange":
        if cmd_item in list:
            list.remove(cmd_item)
            list.append(cmd_item)
    command = input()

list_str = [str(x) for x in list]
print(", ".join(list_str))