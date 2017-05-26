import random

print("Think of a number and I will guess it.")
print("If my number is too high type 'too high', and if it's too low type 'too low'.")

guess = random.randint(0, 101)
feedback = input("Is your number " + str(53) + "?")
numbers = []

if feedback == 'too low':
        guess = random.randint(54, 101)
        feedback = input("Is your number " + str(guess) + " ?")
        numbers.append(guess)
        if guess == numbers:
            continue

if feedback == "too high":
    guess = random.randint(0, 53)
    feedback = input("Is your number " + str(guess) + " ?")
    numbers.append(guess)
    if guess == numbers:
        continue

#while feedback == 'too low'
    #guess >= last_guess

print("I got it!")
