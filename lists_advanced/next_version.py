pre_software = input().split('.')
pre_software_int = list(map(lambda x: int(x), pre_software))

if pre_software_int[2] != 9:
    pre_software_int[2] += 1
elif pre_software_int[2] == 9 and pre_software_int[1] != 9:
    pre_software_int[2] = 0
    pre_software_int[1] += 1
elif pre_software_int[2] == 9 and pre_software_int[1] == 9:
    pre_software_int[2] = 0
    pre_software_int[1] = 0
    pre_software_int[0] += 1

post_software_str = [str(x) for x in pre_software_int]
print(".".join(post_software_str))
