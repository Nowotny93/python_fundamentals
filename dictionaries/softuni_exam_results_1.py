def is_not_banned(dictionary: dict, username: str, language: str, points: int):
    if username not in dictionary.keys():
        dictionary[username] = {}
        dictionary[username][language] = []
        dictionary[username][language].append(points)
    else:
        for (key, value) in dictionary.items():
            if language not in value:
                dictionary[username][language] = []
                dictionary[username][language].append(points)
            elif language in value:
                old_points = dictionary[username][language]
                for number in old_points:
                    if points > number:
                        dictionary[username][language] = []
                        dictionary[username][language].append(points)

dictionary = {}
list_courses = []
command = input()

while command != 'exam finished':
    splt_command = command.split('-')
    cmd_username = splt_command[0]
    cmd_language = splt_command[1]
    if cmd_language != 'banned':
        list_courses.append(cmd_language)
        cmd_points = int(splt_command[2])
        is_not_banned(dictionary, cmd_username, cmd_language, cmd_points)
    else:
        del dictionary[cmd_username]
    command = input()

print('Results:')
for (key, value) in sorted(dictionary.items(), key=lambda kvp: kvp[-1]):
    print(f'{key} | {value}')