def palindrome_integers(nums):
    for i in nums:
        number = ",".join(i)
        separate_numbers_in_list = number.split(',')
        for z in separate_numbers_in_list:
            number_as_int = int(z)
            last_number_in_list = int(separate_numbers_in_list[-1])
            if number_as_int == last_number_in_list:
                print(True)
            elif number_as_int != last_number_in_list:
                print(False)
            break

number_as_str = input().split(", ")
palindrome_integers(number_as_str)