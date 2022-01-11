waiting_people = int(input())
current_state = [int(x) for x in input().split(' ')]

no_queue = False

for index in range (0, len(current_state)):
    if current_state[index] == 0:
        if waiting_people < 4:
            current_state[index] += waiting_people
            waiting_people = 0
            no_queue = True
            break
        else:
            waiting_people -= 4
            current_state[index] += 4
    else:
        waiting_people -= 4 - current_state[index]
        current_state[index] += 4 - current_state[index]

current_state_str = [str(x) for x in current_state]

if no_queue == True and current_state[-1] != 4:
    print('The lift has empty spots!')
    print(f'{" ".join(current_state_str)}')
elif no_queue == True and current_state[-1] == 4:
    print(f'{" ".join(current_state_str)}')
else:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(f'{" ".join(current_state_str)}')
