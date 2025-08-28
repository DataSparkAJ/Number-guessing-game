import random

print("Welcome to Number Guessing Game!")
# Step 1: ask difficulty level
level = input("Choose difficulty (easy/hard): ").lower()
if level == "easy":
    number_to_guess = random.randint(1,50)
    max_range = 50
elif level == "hard":
    number_to_guess = random.randint(1,200)
    max_range = 200
else:
    number_to_guess = random.randint(1,100)
    max_range = 100
# Step 2: Initialize variables
attempts = 0
history = []
# Step 3: Game Loop
while True:
    try:
        guess = int(input(f"Guess the number between 1 and {max_range}: "))
        attempts += 1
        history.append(guess)
        if guess < number_to_guess:
            print("Too low!")
        elif guess >number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"You were guesses were {history}.")
            break
    except ValueError:
        print("Please enter a valid number")




