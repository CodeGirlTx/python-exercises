import random

random_num = random.randint(1, 10)
print ("I am thinking of a number between 1 and 10.")
guess = int(input("What's my number?"))
while guess != random_num:
    guess = int(input("Guess again."))
    if guess < random_num:
        print("Number is too low.")
    elif guess > random_num:
        print("Number is too high")
    elif guess == random_num:
        break
print("Finally")
