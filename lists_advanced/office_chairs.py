rooms = int(input())
count = 1
left_chairs = 0
enough_space = True

while count <= rooms:
    chairs_and_visitors = input().split()
    if len(chairs_and_visitors[0]) == int(chairs_and_visitors[1]):
        count +=1
    elif int(chairs_and_visitors[1]) < len(chairs_and_visitors[0]):
        count += 1
        left_chairs += len(chairs_and_visitors[0]) - int(chairs_and_visitors[1])
    elif int(chairs_and_visitors[1]) > len(chairs_and_visitors[0]):
        enough_space = False
        count += 1
        needed_chairs = int(chairs_and_visitors[1]) - len(chairs_and_visitors[0])
        print(f'{needed_chairs} more chairs needed in room {count - 1}')

if enough_space:
    print(f'Game On, {left_chairs} free chairs left')

