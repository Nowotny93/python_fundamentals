symbol1 = input()
symbol2 = input()

result = []

for i in range (ord(symbol1) + 1, ord(symbol2)):
    result.append(chr(i))

print(" ".join(result))