# imports the random module
import random

# sets the variable secret_number to a random number between 1 and 20
secret_number = random.randint(1,20)
# sets needed variables for while loop
guess_count = 0
guess_limit = 5

# defines what to do while guess_count is less than guess_limit
while guess_count < guess_limit:
    print(f'\nyou have {guess_limit - guess_count} guesses left')   # tells user guesses remaining
    guess = int(input('guess a number: '))  # gets user guess input
    guess_count += 1    # adds +1 to the user guess_count
    if guess == secret_number:
        print('Thats right, you won!')
        break   # end the while loop early
    elif guess > secret_number:
        print("Nope, your guess is too high")
    elif guess < secret_number:
        print("Nope, your guess is too low")
# defines what to do when guess_count is no longer less than guess_limit
else:
    print("\nSorry you are out of guesses")
