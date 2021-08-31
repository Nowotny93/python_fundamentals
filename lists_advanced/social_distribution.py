population = list(map(lambda x: int(x), input().split(', ')))
minimum_wealth = int(input())

for number in population:
    if number < minimum_wealth:
        max_number = max(population)
        needed_wealth = minimum_wealth - number
        if max_number - needed_wealth < minimum_wealth:
            print('No equal distribution possible')
            exit()
        else:
            index_of_max_number = population.index(max_number)
            index_of_number = population.index(number)
            population[index_of_max_number] -= needed_wealth
            population[index_of_number] += needed_wealth

print(population)