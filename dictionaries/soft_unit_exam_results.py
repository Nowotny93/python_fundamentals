def is_not_banned(dictionary: dict, username: str, language: str, points: int):
    if username not in dictionary.keys():
        dictionary[username] = {}
        dictionary[username][language] = []
        dictionary[username][language].append(points)
    else:
        for (key, value) in dictionary.items():
            if key == username and language not in value:
                dictionary[username][language] = []
                dictionary[username][language].append(points)
            elif key == username and language in value:
                old_points = dictionary[username][language]
                for number in old_points:
                    if points > number:
                        dictionary[username][language] = []
                        dictionary[username][language].append(points)

def course_count(dictionary: dict, language: str):
    if language not in dictionary.keys():
        dictionary[language] = 1
    else:
        dictionary[language] += 1

dictionary = {}
list_courses = {}
command = input()

while command != 'exam finished':
    splt_command = command.split('-')
    cmd_username = splt_command[0]
    cmd_language = splt_command[1]
    if cmd_language != 'banned':
        cmd_points = int(splt_command[2])
        course_count(list_courses, cmd_language)
        is_not_banned(dictionary, cmd_username, cmd_language, cmd_points)
    else:
        del dictionary[cmd_username]
    command = input()

final_dict = {}
for (key, value) in dictionary.items():
    for (language, points) in value.items():
        for number in points:
            final_dict[key] = number

print('Results:')
for (name, upoints) in sorted(final_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f'{name} | {upoints}')

print('Submissions:')
for (ulanguage, submissions_count) in sorted(list_courses.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f'{ulanguage} - {submissions_count}')