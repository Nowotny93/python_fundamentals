input_operator = input()
first_num = int(input())
second_num = int(input())

def solve(a,b,operator):

    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = round(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result
print(solve(first_num,second_num, input_operator))