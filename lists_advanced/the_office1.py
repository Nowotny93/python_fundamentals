employeеs = input().split(" ")
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employeеs))
filtered = list(filter(lambda x: int(x) >= (sum(employees) / len(employees)), employeеs))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")