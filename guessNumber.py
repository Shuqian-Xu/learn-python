import random

left = input("Please input the lower range: ")
right = input("Please input the upper range: ")
left = int(left)
right = int(right)
r = random.randint(left, right)
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