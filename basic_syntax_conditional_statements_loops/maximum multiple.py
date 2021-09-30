divisor = int(input())
bound = int(input())
num = ''

if bound % divisor == 0:
    num = bound
    print(num)
elif bound % divisor != 0:
    while bound % divisor != 0:
        bound = bound - 1
    else:
        print(bound)
