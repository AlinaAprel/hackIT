def is_palindrome(word):
    return word == word[::-1]

input_word = input("Введите слово: ")
if is_palindrome(input_word) = True:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
