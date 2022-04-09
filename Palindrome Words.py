import os
os.system('cls')

word = input('\nWhat word do you want to know about Palindrome? ')
word = word.lower()
word_ = word[::-1]

if word == word_:
    print("\n",word)
    print("\n",word_)
    print('\nYess!!! This word is Palindrome')
else:
    print("\n",word)
    print("\n",word_)
    print('\nOh!! Dear!! Is not palindrome.')

