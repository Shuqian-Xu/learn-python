import random

r = random.randint(1, 100)
while True:
    guess = input("Please input your guess: ")
    guess = int(guess)
    if guess == r:
        print("You have made the right guess!")
        break
    elif guess < r:
        print("You guess is smaller than the number!")
    else:
        print("You guess is larger than the number!")