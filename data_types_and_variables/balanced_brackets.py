number_of_lines = int(input())

counter_for_opening_brackets = 0
counter_for_closing_brackets = 0
is_consecutive = False

for i in range (1, number_of_lines + 1):
    symbol = input()
    if symbol == '(':
        counter_for_opening_brackets += 1
    elif symbol == ')':
        counter_for_closing_brackets += 1
    if counter_for_opening_brackets - counter_for_closing_brackets == 2:
        is_consecutive = True

if not counter_for_opening_brackets == counter_for_closing_brackets or is_consecutive:
    print('UNBALANCED')
else:
    print('BALANCED')