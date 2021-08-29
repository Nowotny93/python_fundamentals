random_string = input()

my_list = random_string.split()
opposite = []

for i in range (0, len(my_list)):
    number = my_list[i]
    int_number = int(number)
    opposite_number = -int_number
    opposite.append(opposite_number)

print(opposite)