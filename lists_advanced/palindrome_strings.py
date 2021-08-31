random_words = input().split()
palindrome = input()

palindrome_list = []

for i in random_words:
    if i[0] == i[-1]:
        palindrome_list.append(i)

print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')