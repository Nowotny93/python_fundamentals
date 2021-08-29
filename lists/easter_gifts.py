list_with_gifts = input().split(" ")
command = input()

while command != "No Money":
    command_list = command.split()
    current_command = command_list[0]
    type_of_gift = command_list[1]
    if current_command == "OutOfStock":
        for item in range(len(list_with_gifts)):
            if list_with_gifts[item] == type_of_gift:
                list_with_gifts[item] = "None"
    elif current_command == "Required":
        index = int(command_list[2])
        if 0 <= index < (len(list_with_gifts)):
            list_with_gifts[index] = type_of_gift
    elif current_command == "JustInCase":
        list_with_gifts[-1] = type_of_gift
    command = input()

none_counter = 0
for gift in range(len(list_with_gifts)):
    gift -= none_counter
    if gift < len(list_with_gifts):
        if list_with_gifts[gift] == "None":
            none_counter += 1
            list_with_gifts.remove("None")
    else:
        break
print(" ".join(list_with_gifts))



