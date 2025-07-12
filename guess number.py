import random

number= random.randint(1, 100)
attempts = 0

print("Welcome to the Guess the Number game!")

while True:
        
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in {attempts} attempts.")
        break
