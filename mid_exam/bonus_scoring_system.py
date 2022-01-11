import math

count_of_students = int(input())
count_of_lectures = int(input())
add_bonus = int(input())

total_bonus = 0
max_bonus = 0
winning_student = 0

for student in range (1, count_of_students + 1):
    student_attendancies = int(input())
    total_bonus = (student_attendancies / count_of_lectures) * (5 + add_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        winning_student = student_attendancies

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {winning_student} lectures.')