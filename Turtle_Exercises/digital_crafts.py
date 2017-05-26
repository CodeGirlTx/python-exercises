numbers = []
user_num = input("tell me a number and I'll remember it. \n type quit when you want to quit ")

while user_num != "quit":
    user_num = input("tell me a number and I'll remember it. \n type quit when you want to quit ")
    numbers.append(user_num)
print("Here are your numbers:" + str(numbers))
