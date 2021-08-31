word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
word_without_vowels = "".join([letter for letter in word if letter not in vowels])
print(word_without_vowels)