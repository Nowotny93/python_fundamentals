plants = {}

number = int(input())
for i in range(number):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = [rarity]

while True:
    command = input()
    if command == 'Exhibition':
        break
    data = command.split(": ")
    action = data[0]
    data[1] = data[1].split(" - ")
    flower = data[1][0]
    if flower in plants:
        if action == "Rate":
            rating = int(data[1][1])
            plants[flower].append(rating)
        elif action == "Update":
            plants[flower][0] = int(data[1][1])
        elif action == "Reset":
            plants[flower] = [plants[flower][0]]
    else:
        print("error")
for k, v in plants.items():
    if len(v) > 1:
        average = sum(v[1:]) / len(v[1:])
        plants[k] = [v[0]]
        plants[k].append(average)
    else:
        plants[k].append(0)
plants = sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1]))
print("Plants for the exhibition:")
for key, value in plants:
    print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")