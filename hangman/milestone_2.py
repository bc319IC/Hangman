import random

word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("enter single letter")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")