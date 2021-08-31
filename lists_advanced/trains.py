number_of_wagons = int(input())
command = input().split()

train_base = []

for i in range(1, number_of_wagons + 1):
    train_base.append(0)

while command != ['End']:
        if 'add' in command:
            train_base[number_of_wagons -1] += int(command[1])
        elif 'insert' in command:
            index = int(command[1])
            train_base[index] += int(command[2])
        elif 'leave' in command:
            index = int(command[1])
            needed_number = int(train_base[index]) - int(command[2])
            train_base[index] = needed_number
        command = input().split()

print(train_base)