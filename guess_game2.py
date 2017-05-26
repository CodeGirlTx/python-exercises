import random
#random.randit(1,101)

#instructions to the game
print "Think of a number and I will guess it."
print "If my number is too high type 'too high', and if it's too low type 'too low'."
guess1 = str(50)
guess_high = str(25)
guess_low3 = str(40)
guess_high2 = str(10)
gues_high3 = str(60)
guess_low = str(75)
guess_low2 = str(90)


clue = input("Is your number " + guess1 + " ?")


if clue == "too high":
    print("Ok, hold on I am thinking.")
    clue = input("Is your number " + guess_high)
else:
    print("Ok, hold on I am thinking.")
    clue = input("Is your number " + guess_low)

if clue == "too low":
    print("Ok, hold on I am thinking.")
    clue = input("Is your number " + guess_high)

#loop to keep guessing the number
def keep_going():
    while feedback == "too high" or "too low"
        return feedback_fucntion()

    for x in range(1, 101)
    -------------------
#instructions to the game
print "Think of a number and I will guess it."
print "If my number is too high type 'too high', and if it's too low type 'too low'."
#asks for input and stores answer in list
guessed_numbers = []
def guessed():
    while feedback == 'too low' or 'too high':
        input("Is your number " + str(guess) + " ?")
        guessed_numbers.append(guess)

#ask user for in

if feedback = 'too high'
    guess
