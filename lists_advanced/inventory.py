def collect(collection: list, collect_item : str):
    if collect_item in collection:
        return collection
    else:
        collection.append(collect_item)
        return collection

def drop(collection: list, drop_item : str):
    if drop_item in collection:
        collection.remove(drop_item)
        return collection
    else:
        return collection

def combine_items(collection: list, old_item: str, new_item: str):
    if old_item in collection:
        index_for_old_item = 0
        for el in collection:
            if el != old_item:
                index_for_old_item += 1
            else:
                index_for_new_item = index_for_old_item + 1
                collection.insert(index_for_new_item, new_item)
                break
        return collection
    else:
        return collection

def renew(collection: list, renew_item : int):
    if renew_item in collection:
        collection.remove(renew_item)
        collection.append(renew_item)
        return collection
    else:
        return  collection

collecting_items = input().split(', ')
command = input()

while command != "Craft!":
    cmd_args = command.split(" - ")
    cmd_type = cmd_args[0]
    cmd_item = cmd_args[1]
    if cmd_type == 'Collect':
        collecting_items = collect(collecting_items, cmd_item)
    elif cmd_type == "Drop":
        collecting_items = drop(collecting_items, cmd_item)
    elif "Combine" in cmd_type:
        combine_command_splitted = cmd_type.split()
        combine_command_type = combine_command_splitted[0]
        combine_item_splitted = cmd_item.split(':')
        combine_command_item_old = combine_item_splitted[0]
        combine_command_item_new = combine_item_splitted[1]
        collecting_items = combine_items(collecting_items, combine_command_item_old, combine_command_item_new)
    elif cmd_type == "Renew":
        collecting_items = renew(collecting_items, cmd_item)
    command = input()

print(f'{", ".join(collecting_items)}')