g = p1 = p2 = 0
def printboard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0) 
    one = 'X' if xState[1] else ('O' if zState[1] else 1) 
    two = 'X' if xState[2] else ('O' if zState[2] else 2) 
    three = 'X' if xState[3] else ('O' if zState[3] else 3) 
    four = 'X' if xState[4] else ('O' if zState[4] else 4) 
    five = 'X' if xState[5] else ('O' if zState[5] else 5) 
    six = 'X' if xState[6] else ('O' if zState[6] else 6) 
    seven = 'X' if xState[7] else ('O' if zState[7] else 7) 
    eight = 'X' if xState[8] else ('O' if zState[8] else 8) 
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def sum(a,b,c):
    return a + b + c

def checkWinner(xState,zState):
    global g,p1,p2
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            printboard(xState,zState)
            print("Player 1 win the match!")
            p1 = p1 + 1
            g = g + 1
            return 1
        if(sum(zState[win[0]],zState[win[1]],zState[win[2]]) == 3):
            printboard(xState,zState)
            print("Player 2 win the match!")
            p2 = p2 + 1
            g = g + 1
            return 0
    return -1


print("Welcome to Tic Tak Toe")
while(True):
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1
    i = 0
    while(True):
        printboard(xState,zState)
        if turn == 1:
            print("Player 1's chance")
            value = int(input("Enter the number where you want to put this X : "))
            xState[value] = 1
        else:
            print("Player 2's chance")
            value = int(input("Enter the number where you want to put this O : "))
            zState[value] = 1
        if(i>7):
            g = g + 1
            printboard(xState,zState) 
            print("Draw!")
            break
        cwin = checkWinner(xState,zState)
        if(cwin != -1):
            break
        i = i + 1
        turn = 1 - turn
    print("After "+str(g)+"st round:","\nPlayer 1 :",str(p1),"\nPlayer 2 :",str(p2))
    play_again = input("Match Over! Wanna play again (yes/no) : ").lower()
    if play_again != "yes":
        break
