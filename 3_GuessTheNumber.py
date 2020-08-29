# This is a guess the number game.
import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

for guesses in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    print()

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print("Good job! You guessed my number in", guesses, "guesses!")
else:
    print("Nope. The number I was thinking of was", secretNumber)