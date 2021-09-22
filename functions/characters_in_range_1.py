symbol1 = input()
symbol2 = input()

def solve(a, b):
    result = []
    for i in range (ord(a) + 1, ord(b)):
        result.append(chr(i))
    symbols_between = " ".join(result)
    return symbols_between
print(solve(symbol1, symbol2))