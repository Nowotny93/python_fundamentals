def perfect_not_perfect(desired_number):
    sum_elected_numbers = 0
    for i in range (1, desired_number):
        if number % i == 0:
            sum_elected_numbers += i
        else:
            continue

    if sum_elected_numbers == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")

number = int(input())
perfect_not_perfect(number)