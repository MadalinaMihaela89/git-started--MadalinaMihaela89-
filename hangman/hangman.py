import random
from words import word_list
import string


def get_word():
    word = random.choice(word_list)  # randonmly chooses smthing from list

    return word.upper()


def play():
    word = get_word()
    word_completion = "_" * len(word)
    word_letters = set(word)    # keeping track of what's have already guessed in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()   # what the user has guessed
    lives = 6
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd',]) -->  'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ''.join(guessed_letters))
        # what current word is (ie W-RD)
        word_list = [letter if letter in guessed_letters else '_ ' for letter in word]
        print('Current word: ', ''.join(word_list))    # ' '.join(['a', 'b', 'cd']) = 'a b cd'
        user_letter = input("Please guess a letter or word: ").upper()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1   # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
                print(display_hangman(lives))
                print("\n")

        elif user_letter in guessed_letters:
            print("\nYou already guessed the letter. Please try again.")
        else:
            print('\nInvalid character. Please try again.')

    # my while gets here when len(word_letter) == 0 OR when lives == 0

    # something else
    if lives == 0:
        print("Sorry, you ran out of lives. The word was " + word + ". Maybe next time!")
    else:
        print('Congrats, you guessed the word', word, '. You win!')


def display_hangman(lives):
    stages = ["""
                    ---------
                    |       |
                    |       o
                    |      \\//
                    |       |
                    |      / \\
                    -
                """, """
                    ---------
                    |       |
                    |       o
                    |      \\//
                    |       |
                    |      /
                    -
                """, """
                    ---------
                    |       |
                    |       o
                    |      \\//
                    |       |
                    |
                    -
                """, """
                    ---------
                    |       |
                    |       o
                    |      \\/
                    |       |
                    |
                    -
                """, """
                    ---------
                    |       |
                    |       o
                    |       |
                    |       |
                    |
                    -
                """, """
                    ---------
                    |       |
                    |       o
                    |       |
                    |
                    |
                    -
                """, """
                    ---------
                    |       |
                    |       o
                    |
                    |
                    |
                    -
                """]
    return stages[lives]


if __name__ == "__main__":
    play()
