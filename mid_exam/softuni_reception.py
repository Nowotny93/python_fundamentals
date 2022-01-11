efficiency_employee_one = int(input())
efficiency_employee_two = int(input())
efficiency_employee_three = int(input())
students_count = int(input())

total_sudents_per_hour = efficiency_employee_one + efficiency_employee_two + efficiency_employee_three
hours = 0

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        students_count -= total_sudents_per_hour

print(f'Time needed: {hours}h.')


