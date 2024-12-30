import random
import math

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
print("We'll see how many tries it takes you to guess it!")

number = random.randint(1,100)

print("\nPlease select the difficulty level:")
print("1. Easy (10 tries)")
print("2. Medium (5 tries)")
print("3. Hard (3 tries)")

difficulty = int(input("\nPlease enter the difficulty level: "))
if difficulty == 1:
    tries = 10
elif difficulty == 2:
    tries = 5
elif difficulty == 3:
    tries = 3
print("You have", tries, "tries to guess the number")

for i in range(tries):
    guess = int(input("\nPlease enter your guess: "))
    if guess == number:
        print("\nCongratulations! You guessed the number!")
        print("It took you", i+1, "tries")
        break
    elif guess > number:
        print("\nNumber is less than", guess )
    elif guess < number:
        print("\nNumber is higher than", guess)
    else:
        print("\nInvalid input. Please enter a number between 1 and 100")
        continue

print("\nGame Over! No More Tries")
print("The number was:", number)