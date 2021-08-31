def last_position_cupid(collection: list, index: int):
    if collection[index] == 0:
        lp = index
        return lp
    return index

def already_had_valentine_or_not(collection: list,word: str, index: int):
        if collection[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            collection[index] -= 2
            if collection[index] == 0:
                print(f"Place {index} has Valentine's day.")
        return  collection

houses = input().split('@')
numbers = [int(num) for num in houses]
command = input()
final_index = 0
is_successsful = True
count = 0
last_position = 0

while command != "Love!":
    cmd_args = command.split()
    cmd_command = str(cmd_args[0])
    index = int(cmd_args[1])
    final_index += index
    if final_index > len(numbers) - 1:
        final_index = 0
    if cmd_command == "Jump":
        houses = already_had_valentine_or_not(numbers, cmd_command, final_index)
        last_position = last_position_cupid(numbers, final_index)
    command = input()

for el in numbers:
    if el == 0:
        is_successsful = True
    else:
        is_successsful = False
        break

if is_successsful:
    print(f"Cupid's last position was {last_position}.")
    print('Mission was successful.')
elif not is_successsful:
    for el in numbers:
        if el != 0:
            count += 1
    print(f"Cupid's last position was {last_position}.")
    print(f'Cupid has failed {count} places.')
