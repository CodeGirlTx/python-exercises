def play_again():
    answer = input("Do you want to play again? (Y or N)")
    if answer == "Y":
        return True
    else:
        return False

play_again(print(play_again()))
