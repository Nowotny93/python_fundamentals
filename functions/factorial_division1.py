def factorial_1(a: int):
    a_sum = 0
    for i in range(a - 1, 0, -1):
        a_sum = 0
        a_sum += i * a
        a = a_sum
    return a_sum

def factorial_2(b: int):
    b_sum = 0
    for z in range (b - 1, 0, -1):
        b_sum = 0
        b_sum += z * b
        b = b_sum
    return b_sum

def division(data_a_sum, data_b_sum):
    result = data_a_sum / data_b_sum
    return result

num_1 = int(input())
num_2 = int(input())
data = factorial_1(num_1)
data_2 = factorial_2(num_2)
print("{:.2f}".format(division(data, data_2)))