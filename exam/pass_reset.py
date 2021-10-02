random_string = input()
command = input()

while command != "Done":
    cmd_splt = command.split(' ')
    cmd_type = cmd_splt[0]
    if cmd_type == 'TakeOdd':
        new_pass = ''
        index = 0
        for ch in random_string:
            if index % 2 != 0:
                new_pass += ch
            index += 1
        random_string = new_pass
        print(random_string)
    elif cmd_type == 'Cut':
        cmd_index = int(cmd_splt[1])
        cmd_length = int(cmd_splt[2])
        left_side = random_string[:cmd_index]
        right_side = random_string[(cmd_index + cmd_length):]
        sliced_pass = left_side + right_side
        random_string = sliced_pass
        print(random_string)
    elif cmd_type == 'Substitute':
        cmd_substring = cmd_splt[1]
        cmd_substitute = cmd_splt[2]
        if cmd_substring in random_string:
            random_string = random_string.replace(cmd_substring, cmd_substitute)
            print(random_string)
        else:
            print('Nothing to replace!')
    command = input()

print(f'Your password is: {random_string}')