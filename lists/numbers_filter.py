lines = int(input())

odds = []
evens = []
positives = []
negatives = []

for i in range (1, lines + 1):
    number = int(input())
    if number % 2 == 0:
        evens.append(number)
    if number % 2 != 0:
        odds.append(number)
    if number >= 0:
        positives.append(number)
    if number < 0:
        negatives.append(number)

command = input()
if command == 'even':
    print(evens)
elif command == 'odd':
    print(odds)
elif command == 'positive':
    print(positives)
elif command == 'negative':
    print(negatives)
