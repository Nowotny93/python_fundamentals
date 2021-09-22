def solve(pass_in_list):
    counter_digits = 0
    counter_letters = 0
    for i in pass_in_list:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            counter_digits += 1
        elif i != '0' or i != '1' or i != '2' or i != '3' or i != '4' or i != '5' or i != '6' or i != '7' or i != '8' or i != '9':
            counter_letters += 1

    if counter_digits >= 2 and counter_letters != 0 and len(pass_in_list) >= 6 and len(pass_in_list) <= 10:
        print('Password is valid')
    else:
        if len(pass_in_list) < 6 or len(pass_in_list) > 10:
            print('Password must be between 6 and 10 characters')
        if (counter_digits == 0 and counter_letters != 0) or (counter_digits != 0 and counter_letters == 0):
            print('Password must consist only of letters and digits')
        if counter_digits < 2:
            print('Password must have at least 2 digits')

password = input()
password_separated = ",".join(password)
password_separated_in_list = password_separated.split(",")
solve(password_separated_in_list)