from colorama import init, Fore, Back, Style
from os import system
system("cls")
init()
board=[]
a=[]
for i in range(7):
    a.append("")
for i in range(6):
    board.append(a)
player_1=input((Fore.MAGENTA)+"Player 1, what is your name?\n")
player_2=input((Fore.MAGENTA)+"Player 2, what is your name?\n")
def print_board(board):
    for i in range(len(board)):
        print((Fore.BLUE)+"  "+"-"*29)
        print((Fore.BLUE)+str(len(board)-i)+" |",end="")
        for j in range(len(board[0])):
            if board[i][j]!="":
                print((Fore.BLUE)+" "+a[i][j]+"O"+(Fore.BLUE)+" |",end="")
            else:
                print((Fore.BLUE)+" O |",end="")    
        print("")
    print((Fore.BLUE)+"  "+"-"*29)
def turn(player):
    print_board(board)
    print((Fore.MAGENTA)+"Your turn, %s."%(player))
    print("What row would you like to ")
turn(player_1)
input("")