type = input()
quantity = int(input())

def solve(a,operator):
    result = None
    if operator == 'coffee':
        result = a * 1.50
    elif operator == 'water':
        result = a * 1.00
    elif operator == 'coke':
        result = a * 1.40
    elif operator == 'snacks':
        result = a * 2.00
    return "{:.2f}".format(result)
print(solve(quantity, type))