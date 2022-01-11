price_ratings = [int(x) for x in input().split(', ')]
entry_point = int(input())
type_of_items = input()

entry_point_value = price_ratings[entry_point]
left_items = 0
right_items = 0

for el_left in range (0, entry_point):
    if type_of_items == "cheap":
        if price_ratings[el_left] < entry_point_value:
            left_items += price_ratings[el_left]
    elif type_of_items == "expensive":
        if price_ratings[el_left] >= entry_point_value:
            left_items += price_ratings[el_left]

for el_right in range (entry_point + 1, len(price_ratings)):
    if type_of_items == "cheap":
        if price_ratings[el_right] < entry_point_value:
            right_items += price_ratings[el_right]
    elif type_of_items == "expensive":
        if price_ratings[el_right] >= entry_point_value:
            right_items += price_ratings[el_right]

if right_items > left_items:
    print(f'Right - {right_items}')
elif left_items > right_items:
    print(f'Left - {left_items}')
elif right_items == left_items:
    print(f'Left - {left_items}')