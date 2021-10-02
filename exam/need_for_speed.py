number_of_cars = int(input())

dictionary = {}

for i in range (0, number_of_cars):
    cars_mileage_fuel = input().split('|')
    car = cars_mileage_fuel[0]
    mileage = int(cars_mileage_fuel[1])
    fuel = int(cars_mileage_fuel[2])
    dictionary[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while command != "Stop":
    cmd_splt = command.split(" : ")
    if cmd_splt[0] == 'Drive':
        drive_car = cmd_splt[1]
        drive_distance = int(cmd_splt[2])
        drive_fuel = int(cmd_splt[3])
        if drive_fuel > dictionary[drive_car]['fuel']:
            print('Not enough fuel to make that ride')
        elif drive_fuel <= dictionary[drive_car]['fuel']:
            dictionary[drive_car]['mileage'] += drive_distance
            dictionary[drive_car]['fuel'] -= drive_fuel
            print(f'{drive_car} driven for {drive_distance} kilometers. {drive_fuel} liters of fuel consumed.')
            if dictionary[drive_car]['mileage'] >= 100000:
                del dictionary[drive_car]
                print(f'Time to sell the {drive_car}!')
    elif cmd_splt[0] == 'Refuel':
        refuel_car = cmd_splt[1]
        refuel_fuel = int(cmd_splt[2])
        if refuel_fuel + dictionary[refuel_car]['fuel'] >= 75:
            needed_fuel = 75 - dictionary[refuel_car]['fuel']
            dictionary[refuel_car]['fuel'] += 75 - dictionary[refuel_car]['fuel']
            print(f"{refuel_car} refueled with {needed_fuel} liters")
        else:
            dictionary[refuel_car]['fuel'] += refuel_fuel
            print(f'{refuel_car} refueled with {refuel_fuel} liters')
    elif cmd_splt[0] == 'Revert':
        revert_car = cmd_splt[1]
        revert_km = int(cmd_splt[2])
        dictionary[revert_car]['mileage'] -= revert_km
        if dictionary[revert_car]['mileage'] < 10000:
            dictionary[revert_car]['mileage'] = 10000
        else:
            print(f'{revert_car} mileage decreased by {revert_km} kilometers')
    command = input()

sorted_result = sorted(dictionary.items(), key=lambda tkvp: (-tkvp[1]['mileage'], tkvp[0]))
for car, data in sorted_result:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")