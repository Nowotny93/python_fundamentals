electrons = int(input())

electrons_total = 0
shells_list = []

for i in range (1, electrons + 1):
    max_electrons = 2 * (i * i)
    if electrons > electrons_total:
        shells_list.append(max_electrons)
        electrons_total += max_electrons
        electrons -= max_electrons
    elif electrons <= 0:
        break
    else:
        shells_list.append(electrons)
        break

print(shells_list)


