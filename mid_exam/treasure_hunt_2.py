items = input().split("|")
stolen = []
command = input()
while not command == "Yohoho!":
    command_info = command.split()
    name = command_info[0]
    if name == "Loot":
        for item in range(1, len(command_info)):
            current_item = command_info[item]
            if current_item not in items:
                items.insert(0, current_item)
    if name == "Drop":
        index = int(command_info[1])
        if 0 <= index < len(items):
            x = items.pop(index)
            items.append(x)
    if name == "Steal":
        count = int(command_info[1])
        if count >= len(items):
            print(", ".join(items))
            items = []
        else:
            print(", ".join(items[len(items) - count:]))
            items = items[:len(items) - count]
# принтираме последните три елементи от 8 бр на листа: 8-3 =5 до края(:), а след това отстаналите: от позиция 0 (:) до 8-3=5 без 5
    command = input()
if len(items) == 0:
    print("Failed treasure hunt.")
else:
    sum_length = 0
    for item in items:
        sum_length += len(item)
    print(f"Average treasure gain: {sum_length/len(items):.2f} pirate credits.")