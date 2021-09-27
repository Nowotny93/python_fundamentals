c_dict = {}
command = input()

while command != 'End':
    splt_command = command.split(' -> ')
    company, id = splt_command[0], splt_command[1]
    if company not in c_dict.keys():
        c_dict[company] = []
    if id not in c_dict[company]:
        c_dict[company].append(id)
    command = input()

for (key, value) in sorted(c_dict.items(), key = lambda kvp: kvp[0]):
    print(key)
    for id in value:
        print(f'-- {id}')