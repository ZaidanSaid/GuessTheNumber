# A mini-game, in which you have 5 chances to guess the secret number, ranging from 1-20.

import random

while True:
    print("Greetings, please enter your name.")
    name = input()

    print("Hello " + name + ", I am currently thinking of a number between 1-20. You have 5 chances to guess the number.")
    number = random.randint(1, 20)  # Randomly generates a number between 1-20

    try:
        for guessestaken in range(1, 6):  # 5 guesses
            tries = 6 - guessestaken
            if tries == 1:
                print("give it a shot." + " " + str(tries) + " more attempt.")
            else:
                print("give it a shot." + " " + str(tries) + " more attempts.")
            guess = int(input())
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("too high")
            else:
                break  # Means that the user has guessed correctly, and breaks the loop
    except:
        print("You did not enter a number.")

    try:
        if number == guess:
            print("Congratulations, you guessed correctly!")
            print("The number was indeed " + str(number))
        else:
            print("You have used up your attempts...")
    except:
        ("...")

    # Choice for resetting the game
    print("Do you wish to play again? 1(Yes)/2(No)")
    answer = input()
    if answer == str(1):
        continue  # Goes back to the beginning of the program
    elif answer == str(2):
        print("Thank you for playing.")
        break  # Stops the program
    else:
        print("Invalid input")
        break  # Stops the Program
