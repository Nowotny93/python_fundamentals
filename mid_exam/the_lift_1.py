waiting_people = int(input())
current_state = [int(x) for x in input().split()]

is_full = False

for i in range(0, len(current_state)):
    if waiting_people >= 4:
        if current_state[i] == 0:
            current_state[i] += 4
            waiting_people -= 4
        else:
            quantity = 4 - current_state[i]
            current_state[i] += quantity
            waiting_people -= quantity
    else:
        if current_state[i] == 0:
            current_state[i] += waiting_people
            waiting_people = 0
            break
        else:
            quantity = 4 - current_state[i]
            if waiting_people >= quantity:
                current_state[i] += quantity
                waiting_people = 0
                break
            else:
                current_state[i] += waiting_people
                waiting_people = 0
                break

for i in current_state:
    if i == 4:
        is_full = True
    else:
        is_full = False

current_state_str = [str(x) for x in current_state]

if waiting_people == 0 and is_full == False:
    print("The lift has empty spots!")
    print(" ".join(current_state_str))
elif waiting_people != 0 and is_full:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(" ".join(current_state_str))
elif waiting_people == 0 and is_full:
    print(" ".join(current_state_str))