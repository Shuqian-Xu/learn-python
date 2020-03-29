import random

r = random.randint(1, 100)
count = 0

while True:
    count += 1
    guess = input("Please input your guess: ")
    guess = int(guess)
    if guess == r:
        print("You have made the right guess with", count, "guesses!")
        break
    elif guess < r:
        print("You guess is smaller than the number!")
    else:
        print("You guess is larger than the number!")