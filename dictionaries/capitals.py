countries = input().split(", ")
capitals = input().split(", ")

my_zipped_dictionary = dict(zip(countries, capitals))

for (keys, values) in my_zipped_dictionary.items():
    print(f'{keys} -> {values}')