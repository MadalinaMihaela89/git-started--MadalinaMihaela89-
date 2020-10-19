import random  # Random Module
a = []  # assign an empty list to variable a
a.append(random.randint(1, 99))  # Adding to the list a random number
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
for i in range(10):
    # Asks  the user to guess the number and input a number
    g = int(input("Enter an integer from 1 to 99: "))
    # This while loop will continue running until playerGuess is equal to the random number selected by the computer.
    while a[i] != g:
        # This if statement will check if the number the user chose is less than the random number.
        # If the players guess is too low, it will print out guess is low! Guess Again, allowing the user to guess another number.
        if g < a[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        # This if statement will check if the number the user chose is greater than the random number.
        # If the players guess is too high, it will print out guess is high! Guess again, allowing the user to guess another number.
        elif g > a[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break  # Stops the loop
    # If the players guess is equal to the random number the loop will end.
    print("you guessed it!")

b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
