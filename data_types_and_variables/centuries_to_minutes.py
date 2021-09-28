century = int(input())

centuries_to_years = century * 100
centuries_to_days = int(centuries_to_years * 365.2422)
centuries_to_hours = centuries_to_days * 24
centuries_to_minutes = centuries_to_hours * 60

print(f'{century} centuries = {centuries_to_years} years = {centuries_to_days} days = {centuries_to_hours} hours = {centuries_to_minutes} minutes')