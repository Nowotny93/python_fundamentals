command = input()

while command != 'end':
    list_command = [x for x in command]
    list_command.reverse()
    reversed_command_joined = "".join(list_command)
    print(f'{command} = {reversed_command_joined}')
    list_command.clear()
    command = input()