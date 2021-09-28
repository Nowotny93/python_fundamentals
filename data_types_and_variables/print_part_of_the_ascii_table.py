begin_number = int(input())
end_number = int(input())

sum_symbols = ''

for i in range (begin_number, end_number + 1):
    sum_symbols += ('' + chr(i)  + ' ')

print(f"{sum_symbols}", end = " ")