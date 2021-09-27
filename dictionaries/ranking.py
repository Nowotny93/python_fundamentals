contest_pass = input()

dict_cp = {}
contest_is_valid = False
while contest_pass != 'end of contests':
    contest_pass_splt = contest_pass.split(':')
    dict_cp[contest_pass_splt[0]] = contest_pass_splt[1]
    contest_pass = input()

contest_pass_name_points = input()

dict_np = {}
while contest_pass_name_points != 'end of submissions':
    contest_pass_name_points_splt = contest_pass_name_points.split('=>')
    for (key, value) in dict_cp.items():
        if contest_pass_name_points_splt[0] == key and contest_pass_name_points_splt[1] == value:
            contest_is_valid = True
            break
        else:
            contest_is_valid = False
    if contest_is_valid:
        if contest_pass_name_points_splt[2] not in dict_np.keys():
            dict_np[contest_pass_name_points_splt[2]] = {}
            points = int(contest_pass_name_points_splt[-1])
            dict_np[contest_pass_name_points_splt[2]][contest_pass_name_points_splt[0]] = points
        elif contest_pass_name_points_splt[2] in dict_np.keys():
            for (key, value) in dict_np.items():
                if key == contest_pass_name_points_splt[2]:
                    for (el, p) in value.items():
                        if contest_pass_name_points_splt[0] == el:
                            new_points = int(contest_pass_name_points_splt[-1])
                            if new_points > p:
                                dict_np[contest_pass_name_points_splt[2]][contest_pass_name_points_splt[0]] = new_points
                                break
                            else:
                                break
                        else:
                            dict_np[contest_pass_name_points_splt[2]][contest_pass_name_points_splt[0]] = int(contest_pass_name_points_splt[-1])
                        break
                    break
    contest_pass_name_points = input()

total_points_dict = {}
for (key, value) in dict_np.items():
    total_points_dict[key] = sum(x for x in value.values())

total_points_dict_sorted = dict(sorted(total_points_dict.items(), key=lambda x: -x[1]))
for (key, value) in total_points_dict_sorted.items():
    print(f'Best candidate is {key} with total {value} points.')
    break

dict_np_by_name = dict(sorted(dict_np.items(), key=lambda kvp: kvp[0]))
print('Ranking:')
for (key, value) in dict_np_by_name.items():
    print(key)
    final_dict = dict(sorted(value.items(), key=lambda kvp: -kvp[1]))
    for (i, z) in final_dict.items():
        print(f'#  {i} -> {z}')