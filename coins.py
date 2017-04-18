answer = ''
count = 0
print("You have 0 coins")
answer = input("Do you want another coin?")
while answer == 'yes':
    count += 1
    print("You have " + str(count) + " coins")
    answer = input("Do you want another coin?")

print ("Bye")
