import random

class Hangman():
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess
                    self.num_letters -=1
            #print(self.word_guessed)
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.\nYou have {self.num_lives} lives left.\n")
        print(self.word_guessed)

    def ask_for_input(self):
        while True:
            guess = input("guess a letter\n")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(game.word_guessed)
    while True:
        #print(game.num_lives,game.num_letters)
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)