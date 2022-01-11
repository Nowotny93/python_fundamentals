elements = input().split()
command = input()

moves = 0

while command != "end" and len(elements) > 0:
    moves += 1
    command_splitted = command.split()
    first_index = int(command_splitted[0])
    second_index = int(command_splitted[1])
    middle_index = len(elements) // 2
    if not 0 <= first_index < len(elements) or not 0 <= second_index < len(elements) or first_index == second_index:
        elements.insert(middle_index, f'-{moves}a')
        elements.insert(middle_index, f'-{moves}a')
        print('Invalid input! Adding additional elements to the board')
    else:
        if elements[first_index] == elements[second_index]:
            item = elements[first_index]
            item_2 = elements[second_index]
            elements.remove(item)
            elements.remove(item_2)
            print(f'Congrats! You have found matching elements - {item}!')
        elif elements[first_index] != elements[second_index]:
            print('Try again!')
    command = input()

elements_str = [str(x) for x in elements]

if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements_str))
else:
    print(f"You have won in {moves} turns!")