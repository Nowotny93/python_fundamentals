import math

def is_index_valid(collection: list, zero_index: int, first_index: int):
    if 0 <= zero_index < len(collection) and 0 <= first_index < len(collection) and zero_index != first_index:
        return True
    return False

def replacing_func(collection: list, zero_index: int, first_index: int):
    if collection[zero_index] == collection[first_index]:
        if first_index == 0:
            item = collection.pop(zero_index)
            collection.pop(first_index)
            print(f'Congrats! You have found matching elements - {item}!')
        else:
            item = collection.pop(zero_index)
            collection.pop(first_index - 1)
            print(f'Congrats! You have found matching elements - {item}!')
    else:
        print('Try again!')
    return collection

def add_el_func(collection: list, elements: int):
    middle = math.ceil(len(collection) / 2)
    for i in range (1, elements + 1):
        collection.insert(middle, f'-{elements}a')
    print('Invalid input! Adding additional elements to the board')
    return collection

numbers = input().split()
indexes = input()
moves = 0

while indexes != 'end' and len(numbers) != 0:
    indexes_splitted = indexes.split(' ')
    cmd_zero_index = int(indexes_splitted[0])
    cmd_first_index = int(indexes_splitted[1])
    moves += 1
    is_index_valid(numbers, cmd_zero_index, cmd_first_index)
    if is_index_valid(numbers, cmd_zero_index, cmd_first_index):
        numbers = replacing_func(numbers, cmd_zero_index, cmd_first_index)
    else:
        numbers = add_el_func(numbers, moves)
    indexes = input()

if indexes != "end":
    print(f'You have won in {moves} turns!')
else:
    print('Sorry you lose :(')
    print(f'{" ".join(numbers)}')