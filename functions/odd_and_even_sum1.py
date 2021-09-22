def odd_and_even(nums: str):
   sum_even = 0
   sum_odd = 0
   for ch in nums:
       number = int(ch)
       if number % 2 == 0:
           sum_even += number
       elif number % 2 != 0:
           sum_odd += number
   print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')

number_as_str = input()
odd_and_even(number_as_str)