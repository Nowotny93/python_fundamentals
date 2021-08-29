number = int(input())
lines = int(input())

result = []

for i in range (number, number*lines + 1, number):
    result.append(i)

print(result)
