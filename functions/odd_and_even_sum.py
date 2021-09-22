def odd_and_even(nums: str):
   sum_even = 0
   sum_odd = 0
   for i in nums:
       number = int(i)
       if number % 2 == 0:
           sum_even += number
       elif number % 2 != 0:
           sum_odd += number
   print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')

number_as_str = input()
numbers_separated = " ".join(number_as_str)
numbers_in_list = numbers_separated.split()
odd_and_even(numbers_in_list)



