from colorama import init, Fore, Back, Style
from os import system
system("cls")
init()
board=[]
for i in range(42):
    board.append("")
print(board)
player_1=input((Fore.MAGENTA)+"Player 1, what is your name?\n")
player_2=input((Fore.MAGENTA)+"Player 2, what is your name?\n")
alphabet={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
def print_board(board):
    for i in range(6):
        #prints row by row
        print((Fore.BLUE)+"  "+"-"*29)
        print((Fore.BLUE)+str(6-i)+" |",end="")
        for j in range(7):
            if board[i*7+j]!="":
                print((Fore.BLUE)+" "+board[i*7+j]+"O"+(Fore.BLUE)+" |",end="")
            else:
                print((Fore.BLUE)+"   |",end="")    
        print("")
    print((Fore.BLUE)+"  "+"-"*29)
    print("    A   B   C   D   E   F   G")
def put_counter_in(player,row):
    global board
    holder=True
    for i in range(6):
        if board[(5-i)*7+row]=="" and holder:
            if player==player_1:
                board[(5-i)*7+row]=(Fore.YELLOW) 
            else:
                board[(5-i)*7+row]=(Fore.RED)
            holder=False
    if holder:
        print("Sorry, that column is full.")
        row_2=input("What column would you like to put your token in?\n")
        row_2=alphabet[row_2.upper()]-1
        put_counter_in(player,row_2)
def turn(player):
    print_board(board)
    print((Fore.MAGENTA)+"Your turn, %s."%(player))
    row=input("What column would you like to put your token in?\n")
    row=alphabet[row.upper()]-1
    put_counter_in(player,row)
    if player==player_1:
        turn(player_2)
    else:
        turn(player_1)
    for i in range(3):
        for j in range(7):
            if board[i*7+j]==board[(i+1)*7+j] and board[(i+1)*7+j]==board[(i+2)*7+j] and board[(i+2)*7+j]==board[(i+3)*7+j] and board[i*7+j]!="":
                if board[i*7+j]==(Fore.RED):
                    #player 2 wins
                    print("Winner")
                    pass
                else:
                    print("Winner")
                    #player 1 wins
                    pass
turn(player_1)
input("")