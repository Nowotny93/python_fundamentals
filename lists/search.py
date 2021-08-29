lines = int(input())
secret_word = input()

list = []

for i in range (1, lines + 1):
    random_words = input()
    list.append(random_words)

print(list)

for z in range(len(list) - 1, -1, -1):
    if secret_word not in list[z]:
        list.remove(list[z])

print(list)

