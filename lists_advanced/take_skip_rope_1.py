secret_message = input()

numeric_list = []
non_numeric_list = []
copied_non_numeric_string = non_numeric_list
take_list = []
skip_list = []
concatenated_list = []
taken_letters = []
skipped_lettes = []

for ch in secret_message:
    if ch.isnumeric():
        numeric_list.append(ch)
    else:
        non_numeric_list.append(ch)

numeric_list_int = [int(x) for x in numeric_list]

for index in range(0, len(numeric_list_int)):
    if index % 2 == 0:
        take_list.append(numeric_list_int[index])
    elif index % 2 != 0:
        skip_list.append(numeric_list_int[index])

for index in range(0, len(take_list)):
    concatenated_list.append(take_list[index])
    concatenated_list.append(skip_list[index])
