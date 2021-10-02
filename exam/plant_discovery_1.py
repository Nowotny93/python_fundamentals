number = int(input())

dictionary = {}
counter = 0

for i in range (0, number):
    command = input().split('<->')
    plant = command[0]
    rarity = int(command[1])
    dictionary[plant] = {'Rarity': rarity, 'Rating': 0, 'Count': 0}

cmd = input()
count_rate = 0
while cmd != 'Exhibition':
    cmd_splt = cmd.split(': ')
    if cmd_splt[0] == 'Rate':
        plant_rating = cmd_splt[1]
        plant_rating_splt = plant_rating.split(' - ')
        plant = plant_rating_splt[0]
        rating = int(plant_rating_splt[1])
        dictionary[plant]['Rating'] += rating
        dictionary[plant]['Count'] += 1
        count_rate += 1
    elif cmd_splt[0] == 'Update':
        plant_new_rarity = cmd_splt[1]
        plant_new_rarity_splt = plant_new_rarity.split(' - ')
        plant = plant_new_rarity_splt[0]
        new_rarity = int(plant_new_rarity_splt[1])
        dictionary[plant]['Rarity'] = new_rarity
    elif cmd_splt[0] == 'Reset':
        plant = cmd_splt[1]
        dictionary[plant]['Rating'] = 0
    cmd = input()

if count_rate == 0:
    print('error')
    exit()

for el in dictionary:
    dictionary[el]['Rating'] = (dictionary[el]['Rating']) / (dictionary[el]['Count'])

sorted_result = sorted(dictionary.items(), key=lambda tkvp: (-tkvp[1]['Rarity'], -tkvp[1]['Rating']))
print('Plants for the exhibition:')
for (plant, data) in sorted_result:
    print(f"- {plant}; Rarity: {data['Rarity']}; Rating: {data['Rating']:.2f}")