secret_words = input().split()

for word in secret_words:
    numbers_in_secret_words = []
    letters_in_secret_words = []
    for ch in word:
        if ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8' or ch == '9':
            numbers_in_secret_words.append(ch)
        else:
            letters_in_secret_words.append(ch)
    numbers_in_secret_words_int = list(map(lambda x: int(x), numbers_in_secret_words))
    numbers_in_secret_words_str = [str(x) for x in numbers_in_secret_words_int]
    numbers_in_secret_words_str_joined = "".join(numbers_in_secret_words_str)
    number_in_word = int(numbers_in_secret_words_str_joined)
    ascii_in_word = chr(number_in_word)
    letters_in_secret_words[0], letters_in_secret_words[-1] = letters_in_secret_words[-1], letters_in_secret_words[0]
    letters_in_secret_words.insert(0, ascii_in_word)
    final_word = "".join(letters_in_secret_words)
    print(final_word, end=" ")