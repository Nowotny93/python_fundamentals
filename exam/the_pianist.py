def add_func(collection: dict, song: str, autor: str, accord: str):
    if song in collection.keys():
        print(f'{song} is already in the collection!')
    else:
        collection[song] = {}
        collection[song][autor] = []
        collection[song][autor].append(accord)
        print(f'{song} by {autor} in {accord} added to the collection!')

def remove_func(collection: dict, song: str):
    if song not in collection.keys():
        print(f'Invalid operation! {song} does not exist in the collection.')
    else:
        collection.pop(song)
        print(f'Successfully removed {song}!')

def changekey_func(collection: dict, song: str, autor: str, new_accord: str):
    if song not in collection.keys():
        print(f'Invalid operation! {song} does not exist in the collection.')
    else:
        for (key, value) in collection.items():
            if key == song:
                collection[song][autor] = new_accord
                print(f'Changed the key of {song} to {new_accord}!')

pieces = int(input())
dictionary = {}

for i in range(1, pieces + 1):
    string = input().split('|')
    piece = string[0]
    composer = string[1]
    key = string[2]
    dictionary[piece] = {}
    dictionary[piece][composer] = []
    dictionary[piece][composer].append(key)

command = input()
while command != 'Stop':
    command_splt = command.split('|')
    if command_splt[0] == 'Add':
        piece = command_splt[1]
        composer = command_splt[2]
        key = command_splt[3]
        add_func(dictionary, piece, composer, key)
    elif command_splt[0] == 'Remove':
        piece = command_splt[1]
        remove_func(dictionary, piece)
    elif command_splt[0] == 'ChangeKey':
        piece = command_splt[1]
        new_key = command_splt[2]
        changekey_func(dictionary, piece, composer, new_key)
    command = input()

for (key, value) in sorted(dictionary.items(), key=lambda kvp: (kvp[0], kvp[1])):
    print(f'{key} -> Composer:', end=" ")
    for (i, p) in value.items():
        print(f'{i}, Key: {"".join(p)}')