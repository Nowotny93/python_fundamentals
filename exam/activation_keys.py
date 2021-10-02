random_string = input()
command = input()

sliced_string = ''

while command != 'Generate':
    command_splt = command.split('>>>')
    if command_splt[0] == 'Contains':
        if command_splt[1] in random_string:
            print(f'{random_string} contains {command_splt[1]}')
        else:
            print('Substring not found!')
    elif command_splt[0] == 'Flip':
        upper_lower = command_splt[1]
        start_index = int(command_splt[2])
        end_index = int(command_splt[3])
        if upper_lower == 'Upper':
            for i in range (start_index, end_index):
                upper_case = random_string[i].upper()
                sliced_string += upper_case
                #random_string = random_string.replace(random_string[i], upper_case)
        elif upper_lower == 'Lower':
            for p in range(start_index, end_index):
                lower_case = random_string[p].lower()
                sliced_string += lower_case
                #random_string = random_string.replace(random_string[i], lower_case)
        random_string = random_string[:start_index] + sliced_string + random_string[end_index:]
        print(random_string)
        sliced_string = ''
    elif command_splt[0] == 'Slice':
        start_index_slice = int(command_splt[1])
        end_index_slice = int(command_splt[2])
        random_string = random_string[:start_index_slice] + random_string[end_index_slice:]
        print(random_string)
    command = input()

print(f'Your activation key is: {random_string}')