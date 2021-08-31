train_length = int(input())

train = [0] * train_length
command = input()

while command != "End":
    tokens = command.split(" ")
    key_word = tokens[0]
    if key_word == "add":
        train[train_length - 1] += int(tokens[1])
    elif key_word == 'insert':
        index = int(tokens[1])
        train[index] += int(tokens[2])
    elif key_word == 'leave':
        index = int(tokens[1])
        train[index] -= int(tokens[2])
    command = input()

print(train)