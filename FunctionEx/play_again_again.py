def play_again():
    answer = input("Do you want to play again? (Y or N)")
    if answer == "Y":
        return True
    if answer == "N":
        return False
    else:
        print("Invalid Input")
        answer = input("Do you want to Play again? (Y or N)")

play_again()
