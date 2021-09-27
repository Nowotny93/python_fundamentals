commands = int(input())

database = {}

for i in range (1, commands + 1):
    command = input().split()
    cmd_type = command[0]
    cmd_name = command[1]
    if cmd_type == 'register':
        cmd_number = command[2]
        if cmd_name not in database:
            database[cmd_name] = cmd_number
            print(f'{cmd_name} registered {cmd_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {cmd_number}')
    elif cmd_type == "unregister":
        if cmd_name not in database:
            print(f'ERROR: user {cmd_name} not found')
        else:
            print(f'{cmd_name} unregistered successfully')
            del database[cmd_name]

for (key, value) in database.items():
    print(f'{key} => {value}')