concealed_message = input()
command = input()

while command != "Reveal":
    command_splt = command.split(':|:')
    if command_splt[0] == 'InsertSpace':
        index = int(command_splt[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)
    elif command_splt[0] == 'Reverse':
        substring = command_splt[1]
        if substring in concealed_message:
            #concealed_message = concealed_message.split(substring, 1)
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message = concealed_message + substring
            print(concealed_message)
        else:
            print('error')
    elif command_splt[0] == 'ChangeAll':
        substring = command_splt[1]
        replacement = command_splt[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()

print(f'You have a new text message: {concealed_message}')