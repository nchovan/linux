import random

secret_number = random.randint(1,20)
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    print(f'\nyou have {guess_limit - guess_count} guesses left')
    guess = int(input('guess a number: '))
    guess_count += 1
    if guess == secret_number:
        print('Thats right, you won!')
        break
    elif guess > secret_number:
        print("Nope, your guess is too high")
    elif guess < secret_number:
        print("Nope, your guess is too low")

else:
    print("\nSorry you are out of guesses")
