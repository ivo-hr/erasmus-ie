#from cgi import test
import random


# -- LetterColour Class --
# This class is used to store the letter and its colour.

class LetterColour:
    letter: str = ""
    colour: str = ""
    
    def __init__(self, letter, colour):
        self.letter = letter
        self.colour = colour
        
        
# -- Wordle Game --

class WordleGame:
    def __init__(self, word):
        self.word = word
        self.guesses = set()
        self.num_guesses = 0
        self.max_guesses = 6
        self.correct_letters = 0
        self.contained_letters = 0
        self.incorrect_letters = 0
        
        self.game_over = False
        self.won = False

    def play(self, input_word = None):

        print("Welcome to Wordle!")
        print("Guess the word by entering a 5-letter word.")
        print("You have 6 attempts to guess the word.")

        while self.num_guesses < self.max_guesses and not self.won:
            print(self.max_guesses - self.num_guesses, "guesses remaining.")
            if not input_word: 
                guess = input("Enter your guess: ").lower()
            else:
                guess = input_word

            if len(guess) != 5:
                print("Invalid guess. Please enter a 5-letter word.")
                if not input_word: 
                    continue
                else:
                    return

            self.guesses.add(guess)
            self.num_guesses += 1
            self.display_word(guess)
            
            if guess == self.word:
                print("Congratulations! You guessed the word correctly.")
                self.won = True
                #exit()



        if not self.won:
            print("Game over! You ran out of attempts.")
            print(f"The word was: {self.word}")
            self.game_over = True
            #exit()

    def display_word(self, guess, TEST=False):
        self.correct_letters = 0
        self.contained_letters = 0
        self.incorrect_letters = 0
        
        if TEST: 
            testword = []

        position = 0
        for letter in guess:
            if letter in self.word:
                if letter == self.word[position]:
                    colour = "\033[92m"  # Green color
                    self.correct_letters += 1
                    if TEST:
                        letter = letter.capitalize()
                else:
                    colour = "\033[93m"  # Yellow color
                    self.contained_letters += 1
                    if TEST:
                        letter = letter.lower()
            else:
                colour = "\033[90m"  # Gray color
                self.incorrect_letters += 1
                if TEST:
                    letter = "_"

            if not TEST:
                print(f"{colour}{letter.capitalize()}\033[0m", end=" ")
            else:
                testword.append(letter)
            position += 1
        print()
        
        if TEST:
            return "".join(testword)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example usage
if __name__ == "__main__":
    word = random.choice(["apple", "gnoll", "pines", "grape", "melon"])
    game = WordleGame(word)
    game.play()
