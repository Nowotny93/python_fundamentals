encrypted_message = list(input())
command = input()

while command != "Decode":
    command_splt = command.split('|')
    if command_splt[0] == 'Move':
        cmd_number = int(command_splt[1])
        for letter in range (0, cmd_number):
            needed_letter = encrypted_message.pop(letter)
            encrypted_message.insert(letter, 0)
            encrypted_message.append(needed_letter)
        encrypted_message = [str(x) for x in encrypted_message if x != 0]
    elif command_splt[0] == 'Insert':
        cmd_index = int(command_splt[1])
        cmd_value = command_splt[2]
        encrypted_message.insert(cmd_index, cmd_value)
    elif command_splt[0] == 'ChangeAll':
        cmd_substring = command_splt[1]
        cmd_replacement = command_splt[2]
        for ch in encrypted_message:
            if ch == cmd_substring:
                index = int(encrypted_message.index(ch))
                encrypted_message.pop(index)
                encrypted_message.insert(index, cmd_replacement)

    command = input()

print(f'The decrypted message is: {"".join(encrypted_message)}')