houses = [int(x) for x in input().split('@')]
command = input()

variable = 0
valentines_pos = 0
failed_places = 0

while command != "Love!":
    command_splitted = command.split()
    length = int(command_splitted[1])
    if 0 <= length + variable < len(houses):
        for i in range (0, len(houses)):
            if i == length:
                if houses[i] == 0:
                    print(f"Place {i} already had Valentine's day.")
                else:
                    houses[i + variable] -= 2
                    variable += i
                    valentines_pos = variable
                    if houses[variable] == 0:
                        print(f"Place {valentines_pos} has Valentine's day.")
    else:
        variable = 0
        if houses[variable] == 0:
            print(f"Place {variable} already had Valentine's day.")
        else:
            houses[variable] -=2
            valentines_pos = variable
            if houses[variable] == 0:
                print(f"Place {valentines_pos} has Valentine's day.")
    command = input()

for i in houses:
    if i != 0:
        failed_places += 1

print(f"Cupid's last position was {valentines_pos}.")
if sum(houses) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {failed_places} places.")
