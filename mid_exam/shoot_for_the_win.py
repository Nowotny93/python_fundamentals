targets = [int(x) for x in input().split()]
index = input()

shot_targets = 0

while index != "End":
    index_int = int(index)
    if index_int > len(targets) - 1:
        index = input()
        continue
    else:
        data = targets[index_int]
        targets[index_int] = -1
        shot_targets += 1
    for i in range(0, len(targets)):
        if targets[i] > data and targets[i] != -1:
            targets[i] -= data
        elif targets[i] <= data and targets[i] != -1:
            targets[i] += data
    index = input()

targets_str = [str(x) for x in targets]
print(f'Shot targets: {shot_targets} -> {" ".join(targets_str)}')