secret_num = 5
print ("I am thinking of a number between 1 and 10.")
guess = int(input("What's my number?"))
while guess != 5:
    guess = int(input("Guess again."))
    if guess < 5:
        print("Number is too low.")
    elif guess > 5:
        print("Number is too high")
    elif guess == 5:
        break
print("Finally")
