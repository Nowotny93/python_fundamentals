individual_happiness = input().split()
factor = int(input())

individual_happiness_list = list(map(lambda x: int(x), individual_happiness))
individual_happiness_list_multiplied = [x*factor for x in individual_happiness_list]
total_happiness = 0

for i in individual_happiness_list_multiplied:
    total_happiness += i

average_happiness = total_happiness / len(individual_happiness_list_multiplied)

happy_employes = list(filter((lambda x: x >= average_happiness), individual_happiness_list_multiplied))
if len(happy_employes) >= len(individual_happiness_list_multiplied)/2:
    print(f'Score: {len(happy_employes)}/{len(individual_happiness_list_multiplied)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employes)}/{len(individual_happiness_list_multiplied)}. Employees are not happy!')