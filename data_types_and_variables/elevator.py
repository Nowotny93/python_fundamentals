number_people = int(input())
capacity = int(input())

if number_people % capacity == 0:
    print(f'{int(number_people / capacity)}')
elif number_people % capacity != 0:
    print(f'{(number_people // capacity) + 1}')