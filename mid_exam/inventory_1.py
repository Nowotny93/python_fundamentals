journal = input().split(', ')
command = input()

while command != "Craft!":
    command_splt = command.split(' - ')
    cmd_type = command_splt[0]
    cmd_item = command_splt[1]
    if cmd_type == "Collect":
        if cmd_item not in journal:
            journal.append(cmd_item)
    elif cmd_type == "Drop":
        if cmd_item in journal:
            journal.remove(cmd_item)
    elif cmd_type == "Combine Items":
        cmd_item_splt = cmd_item.split(':')
        cmd_old_item = cmd_item_splt[0]
        cmd_new_item = cmd_item_splt[1]
        if cmd_old_item in journal:
            cmd_item_index = journal.index(cmd_old_item)
            needed_index = cmd_item_index + 1
            journal.insert(needed_index, cmd_new_item)
    elif cmd_type == "Renew":
        if cmd_item in journal:
            cmd_item_index = journal.index(cmd_item)
            journal.pop(cmd_item_index)
            journal.append(cmd_item)
    command = input()

print(", ".join(journal))