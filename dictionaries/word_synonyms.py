words = int(input())

dictionary = {}

for i in range(words):
    synonym = input()
    synonym_2 = input()
    if not synonym in dictionary:
        dictionary[synonym] = []
    dictionary[synonym].append(synonym_2)

for i in dictionary:
    print(f'{i} - {", ".join(dictionary[i])}')