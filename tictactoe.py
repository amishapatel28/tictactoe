def printBoard(xstate, zstate):
    def mark(val):
        return 'X' if val == 1 else ('O' if val == -1 else val)

    print(f" {mark(xstate[0])} | {mark(xstate[1])} | {mark(xstate[2])} ")
    print("---|---|---")
    print(f" {mark(xstate[3])} | {mark(xstate[4])} | {mark(xstate[5])} ")
    print("---|---|---")
    print(f" {mark(xstate[6])} | {mark(xstate[7])} | {mark(xstate[8])} ")

def checkwin(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        if sum([xstate[win[0]], xstate[win[1]], xstate[win[2]]]) == 3:
            print("X won the match")
            return 1
        if sum([zstate[win[0]], zstate[win[1]], zstate[win[2]]]) == -3:
            print("O won the match")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to tic-tac-toe")
    
    while True:
        printBoard(xstate, zstate)
        
        if turn == 1:
            print("X's chance")
            value = int(input("Please enter a value: "))
            if xstate[value] == 0:
                xstate[value] = 1
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("O's chance")
            value = int(input("Please enter a value: "))
            if zstate[value] == 0:
                zstate[value] = -1
            else:
                print("Invalid move. Try again.")
                continue
                
        cwin = checkwin(xstate, zstate)
        
        if cwin != -1:
            print("Match over")
            break
            
        turn = 1 - turn
