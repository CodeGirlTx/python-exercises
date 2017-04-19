secret_num = 5

print ("I am thinking of a number between 1 and 10.")
guess_count = 6
while guess_count > 0:
    guess_count -=1
    print("You have " + str(guess_count) + " guesses left.")
    if guess_count == 0:
        print("Sorry, no more guesses")
        break
    guess = int(input("What's my number?"))
    if guess < 5:
        print(str(guess) + " is too low.")
    elif guess > 5:
        print(str(guess) + " is too high")
    elif guess == 5:
        print("You got it!")
        break
