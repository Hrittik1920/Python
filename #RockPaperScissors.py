import random
print("Welcome".center(30," "))
print("To".center(30," "))
print("Rock,Paper & Scissor Game".center(30," "))
print()
while(True):
    choices = ["rock","paper","scissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper & scissor? : ").lower()
    print("Computer :",computer)
    print("player :",player)

    if computer == player:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You Lose!")
        else:
            print("You Win!")
    elif player == "paper":
        if computer == "scissor":
            print("You Lose!")
        else:
            print("You Win!")
    else:
        if computer == "rock":
            print("You Lose!")
        else:
            print("You Win!")
    play_again = input("Play again (yes/no) : ").lower()
    if play_again == "no":
        break
