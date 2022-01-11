def swap_func(collection: list, first_index: int, second_index: int):
    collection[first_index], collection[second_index] = collection[second_index], collection[first_index]
    return collection

def multiply_func(collection: list, first_index: int, second_index: int):
    multiplied_indexes = collection[first_index] * collection[second_index]
    #collection.remove(collection[first_index])
    collection.pop(first_index)
    collection.insert(first_index, multiplied_indexes)
    return collection

def decrease_func(collection: list):
    for el in range(0, len(collection)):
        collection[el] -= 1
    return collection

array = [int(x) for x in input().split()]
command = input()

while command != "end":
    splitted_command = command.split()
    cmd_type = splitted_command[0]
    if cmd_type == "swap":
        cmd_index_1 = int(splitted_command[1])
        cmd_index_2 = int(splitted_command[2])
        array = swap_func(array, cmd_index_1, cmd_index_2)
    elif cmd_type == "multiply":
        cmd_index_1 = int(splitted_command[1])
        cmd_index_2 = int(splitted_command[2])
        array = multiply_func(array, cmd_index_1, cmd_index_2)
    elif cmd_type == "decrease":
        array = decrease_func(array)
    command = input()

array_str = [str(x) for x in array]
print(f'{", ".join(array_str)}')


