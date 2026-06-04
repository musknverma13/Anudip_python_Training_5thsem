from random import *
number = randrange(1, 101)
guess = 0
while guess!= number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
print("Congratulations! You guessed the number! 🎉")
