import random
import sys
import os
import time


def read_file(filename):
    ret = []
    with open(filename) as f:
        ret = [e.split(" | ")[0].strip() for e in f.readlines() if len(e.strip()) > 0]

    return ret


def word_for_level(lista_cuvinte, nivel):
    temp = []
    for word in lista_cuvinte:
        l = len(word)
        if nivel == 1 and l < 5:
            temp.append(word)
        if nivel == 2 and l >= 5 and l < 8:
            temp.append(word)
        if nivel == 3 and l >= 8:
            temp.append(word)

    return temp


def display_word(word, letters_guessed):
    ret = []
    for letter in word:
        if letter.lower() in letters_guessed:
            ret.append(letter)
        else:
            ret.append("_")
    return ret


def play(word):
    pass


def check_win():
    pass


def validate_level():
    nivel = None
    while nivel not in [1, 2, 3]:
        try:
            nivel = int(input("Please choose level 1, 2 or 3: "))
        except ValueError:
            print("Please select 1, 2 or 3")

    return nivel


def game_over(has_won, word):
    if has_won:
        print("Congrats! You won! \n ")
    else:
        print("You lose.")
    print("Your word was " + word)
    cont = input("Want to try again? Y/N ")
    if cont.lower() == "y":
        main()
    else:
        print("Thanks for playing. ")
        sys.exit()


def main():

    os.system("clear")
    words = read_file("countries-and-capitals.txt")
    nivel = validate_level()
    options = word_for_level(words, nivel)
    chosen_word = random.choice(options)

    tried_letters = []

    attempts = 0
    if nivel == 1:
        max_attempts = 6
    elif nivel == 2:
        max_attempts = 5
    elif nivel == 3:
        max_attempts = 4

    while attempts <= max_attempts:
        os.system("clear")
        print(attempts)

        print(display_hangman(attempts, nivel))
        print(
            "Number of tries left:",
            (max_attempts - attempts),
        )  # arata no incercari ramase

        print("\n")
        print(" ".join(display_word(chosen_word, tried_letters)))
        print("\n")
        print("Letters tried so far are: ", " ".join(tried_letters).upper())
        letter = input("Guess a letter! ").lower()

        if letter == chosen_word.lower():
            game_over(True, chosen_word)
        if letter == "quit":
            print("Goodbye. ")
            sys.exit()
        if letter in tried_letters:
            print("Letter already used!")
            time.sleep(1.5)
        else:
            tried_letters.append(letter)

            # sparg iful in 2 etape, una de check, una de display
            # primul if verifica daca litera aleasa se regaseste in cuvantul ales
            contor = 0
            if letter in chosen_word.lower():
                for l in chosen_word.lower():
                    if l in tried_letters:
                        contor += 1
                if contor == len(chosen_word):
                    game_over(True, chosen_word)

            else:
                attempts += 1
            temp = " ".join(display_word(chosen_word, tried_letters))

            print(temp)

            # apoi afisam cuvantul cu _ pt litere nechigicite sau litera in sine daca este ghicita

    else:
        game_over(False, chosen_word)

    print(chosen_word)


def display_hangman(lives, level):

    stages = [
        [
            """
                 ______
                |     '
                |
                |
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |     |
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |    /
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |    / \\
                |
            """,
        ],
        [
            """
                 ______
                |     '
                |     
                |    
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |     |
                |
                |
            """,
            """
                ______
                |     '
                |     O
                |    /|
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |    /
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |    / \\
                |
            """,
        ],
        [
            """
                 ______
                |     '
                |     
                |    
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |     
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |     |
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |
                |
            """,
            """
                 ______
                |     '
                |     O
                |    /|\\
                |    / \\
                |
            """,
        ],
    ]

    return stages[level - 1][lives]

    # if level == 1:
    #     disp = stages
    # elif level == 2:
    #     disp = [stages[0], stages[1], stages[2], stages[4], stages[6]]
    # else:
    #     disp = [stages[0], stages[3], stages[4], stages[6]]

    # return disp[attempts]


if __name__ == "__main__":
    main()
