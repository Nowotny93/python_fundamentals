random_string = input()
my_list = random_string.split()
my_final_list = []

team_a = 11
team_b = 11
terminated = False

for i in my_list:
    if i not in my_final_list:
        my_final_list.append(i)

for z in range (0, len(my_final_list)):
    if "A" in my_final_list[z]:
        team_a -= 1
        if team_a < 7:
            terminated = True
            break
    if "B" in my_final_list[z]:
        team_b -= 1
        if team_b < 7:
            terminated = True
            break

if terminated:
    print(f'Team A - {team_a}; Team B - {team_b}')
    print('Game was terminated')
else:
    print(f'Team A - {team_a}; Team B - {team_b}')