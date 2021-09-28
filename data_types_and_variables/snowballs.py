import sys

min_num = -sys.maxsize

number_of_snowballs = int(input())

snowball_snow_max = 0
snowball_time_max = 0
snowball_quality_max = 0

for i in range (1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    result = (snowball_snow / snowball_time) ** snowball_quality
    if result > min_num:
        min_num = result
        snowball_snow_max = snowball_snow
        snowball_time_max = snowball_time
        snowball_quality_max = snowball_quality

print(f'{snowball_snow_max} : {snowball_time_max} = {min_num:.0f} ({snowball_quality_max})')

