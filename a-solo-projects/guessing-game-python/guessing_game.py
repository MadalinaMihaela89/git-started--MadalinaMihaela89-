import random


def generate_numbers(start, end, list_name):
    for i in range(10):
        list_name.append(random.randint(start, end))


def play_the_game(list_of_numbers, range_end):
    for i in range(10):
        user_number = get_user_input(range_end)
        check_user_input(user_number, list_of_numbers, i, range_end)


def get_user_input(range_end):
    user_number = int(
        input("Enter an integer from 1 to " + str(range_end) + ": ")
    )
    return user_number


def check_user_input(user_number, list_of_numbers, i, range_end):
    while list_of_numbers[i] != user_number:
        if user_number < list_of_numbers[i]:
            print("guess is low")
            user_number = get_user_input(range_end)
        elif user_number > list_of_numbers[i]:
            print("guess is high")
            user_number = get_user_input(range_end)
        else:
            break
    print("you guessed it!")


random_ints_1to99 = []
generate_numbers(start=1, end=99, list_name=random_ints_1to99)
play_the_game(random_ints_1to99, range_end=99)

random_ints_1to49 = []
generate_numbers(start=1, end=49, list_name=random_ints_1to49)
play_the_game(random_ints_1to49, range_end=49)
