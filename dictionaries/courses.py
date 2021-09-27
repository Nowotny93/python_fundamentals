students_dict = {}

command = input()

while ":" in command:
    info = command.split(" :")
    course, name = info[0], info[1]
    if course not in students_dict.keys():
        students_dict[course] = []
    if name not in students_dict[course]:
        students_dict[course].append(name)
    command = input()

sorted_courses = sorted(students_dict.items(), key=lambda kvp: -len(kvp[1]))

for (key, value) in sorted_courses:
    print(f"{key}: {len(value)}")
    result = sorted(value)
    for i in result:
        print(f'--{i}')