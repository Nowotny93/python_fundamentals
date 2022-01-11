dungeons_rooms = input().split('|')

health = 100
bitcoins = 0
counter_rooms = 0
still_alive = True

for room in dungeons_rooms:
    room_splitted = room.split()
    command = room_splitted[0]
    number = int(room_splitted[1])
    if command == 'potion':
        counter_rooms += 1
        health += number
        if health > 100:
            healed_number = 100 - (health - number)
            health = 100
            print(f'You healed for {healed_number} hp.')
            print(f'Current health: {health} hp.')
        else:
            print(f'You healed for {number} hp.')
            print(f'Current health: {health} hp.')
    elif command == 'chest':
        counter_rooms += 1
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        counter_rooms +=1
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            still_alive = False
            print(f'You died! Killed by {command}.')
            print(f'Best room: {counter_rooms}')
            break

if still_alive:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')