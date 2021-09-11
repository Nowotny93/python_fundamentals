usernames = input().split(', ')

len_username = False
alpha_digit = False

for username in usernames:
    if 3 <= len(username) <= 16:
        len_username = True
    else:
        len_username = False
    for ch in username:
        if ch.isalpha() or ch.isdigit() or ch == '_' or ch == '-':
            alpha_digit = True
        else:
            alpha_digit = False
            break

    if len_username == True and alpha_digit == True:
     print(username)
