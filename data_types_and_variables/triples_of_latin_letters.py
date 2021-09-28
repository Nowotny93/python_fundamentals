num = int(input())

for i in range (0, num):
    for m in range (0, num):
        for z in range (0, num):

            print(f'{chr(97 + i)}{chr(97 + m)}{chr(97 + z)}')