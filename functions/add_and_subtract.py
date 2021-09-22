def sum_numbers(a: int, b: int):
    return a + b

def subtract(data, c: int):
    return data - c

num1 = int(input())
num2 = int(input())
num3 = int(input())

data = sum_numbers(num1, num2)
print(subtract(data, num3))