string = input().split()

result = ''

for word in string:
    length_word = len(word)
    output = word * length_word
    result += output

print(result)