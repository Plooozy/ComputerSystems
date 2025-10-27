from random import randrange


def get_number_input(prompt):
    # Valid input function
    guess = input(prompt)
    # Checks if input is a number
    while not guess.isdigit():
        print("You did not enter a number")
        guess = input(prompt)
    guess = int(guess)
    # Checks if input is between 1 and 100
    while guess < 1 or guess > 100:
        print("Number must be between 1 and 100")
        guess = input(prompt)
        while not guess.isdigit():
            print("You did not enter a number")
            guess = input(prompt)
        guess = int(guess)
    return guess


def Guessing():
    random_number = randrange(1, 100)
    print("Guess a number between 1 and 100")
    print("You have 5 attempts")
    guess = get_number_input("Your guess: ")
    count = 1
    while guess != random_number:
        if count > 4:
            print("You are out of guesses")
            print("The number was %d" % random_number)
            break
        if guess < random_number:
            print("Too low, you have %d guesses left" % (5 - count))
        else:
            print("Too high, you have %d guesses left" % (5 - count))
        count += 1
        guess = get_number_input("Another guess: ")
    else:
        print("Congratulations, you guessed the number!")
        print("Random number was: %d" % random_number)
