#function to print tic tac toe board
def printBoard(x,y):
    #condition to check if user entered something at 0 position if user enters nothing on this position then printing the position number
    if(x[0] ==1):
        zero = "X"
    else:
        if(y[0] ==1):
            zero = "O"
        else:
            zero = "0"
    #condition to check if user entered something at 1 position if user enters nothing on this position then printing the position number        
    if(x[1] ==1):
        one = "X"
    else:
        if(y[1] ==1):
            one = "O"
        else:
            one = "1"
    #condition to check if user entered something at 2 position if user enters nothing on this position then printing the position number        
    if(x[2] ==1):
        two = "X"
    else:
        if(y[2] ==1):
            two = "O"
        else:
            two = "2"
    #condition to check if user entered something at 3 position if user enters nothing on this position then printing the position number        
    if(x[3] ==1):
        three = "X"
    else:
        if(y[3] ==1):
            three = "O"
        else:
            three = "3"
    #condition to check if user entered something at 4 position if user enters nothing on this position then printing the position number        
    if(x[4] ==1):
        four = "X"
    else:
        if(y[4] ==1):
            four = "O"
        else:
            four = "4"
    #condition to check if user entered something at 5 position if user enters nothing on this position then printing the position number        
    if(x[5] ==1):
        five = "X"
    else:
        if(y[5] ==1):
            five = "O"
        else:
            five = "5"
    #condition to check if user entered something at 6 position if user enters nothing on this position then printing the position number
    if(x[6] ==1):
        six = "X"
    else:
        if(y[6] ==1):
            six = "O"
        else:
            six = "6"
    #condition to check if user entered something at 7 position if user enters nothing on this position then printing the position number        
    if(x[7] ==1):
        seven = "X"
    else:
        if(y[7] ==1):
            seven = "O"
        else:
            seven = "7"
    #condition to check if user entered something at 8 position if user enters nothing on this position then printing the position number    
    if(x[8] ==1):
        eight = "X"
    else:
        if(y[8] ==1):
            eight = "O"
        else:
            eight = "8"
            
    #printing board with 9 values 
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
#main function    
if __name__ == "__main__":
    #two lists to keep track of where the users entered their input
    xMove = [0,0,0,0,0,0,0,0,0]
    oMove = [0,0,0,0,0,0,0,0,0]
    #printing welcome message
    print("Welcome to Tic Tac Toe\n")
    
    #turn variable to check who's turn it is
    turn = 1
    #a counter for how many moves has been made by both the users
    i=0
    #while loop for changing turns for users until someone wins or all the moves has been exhausted by both users
    while(True):
        #incrementing i for one move made
        i+=1
        #checking if all the moves has been exhausted by both the users if yes then ending the game
        if(i==10):
            print("Match over!! it's a tie!")
            break
        #checking if it's X's turn and taking input from X user to mark their move
        if(turn==1):
            print("X's turn")
            x = int(input("Please enter the position number where you want to mark X: "))
            xMove[x] = 1
        #checking if it's O's turn and taking input from O user to mark their move
        if(turn==0):
            print("O's turn")
            y = int(input("Please enter the position number where you want to mark O: "))
            oMove[y] = 1
        
        #calling function to print board with latest values
        printBoard(xMove, oMove)