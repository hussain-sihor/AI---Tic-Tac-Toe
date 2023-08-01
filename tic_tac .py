from tkinter import *
import random
import time


def minimax(board,depth,ismaximizing):

    # ...........////terminal states
   if (checkwinletter(bot)) :
    return 1
   
   elif (checkwinletter(human) ) :
    return -1
   
   elif (checkdraw())  :
       return 0
   
   if ( ismaximizing) :
        bestscore = -1000
        for key in board.keys() :
           if (board[key] == ' '):
               board[key] = bot
               score = minimax(board,depth+1,False)
               board[key] =' '
               if(score > bestscore) :
                 bestscore = score

        return bestscore
   
   else :
        bestscore = 1000
        for key in board.keys() :
           if (board[key] == ' ') :
                 board[key] = human
                 score = minimax(board,depth+1,True)
                 board[key]=' '
                 if(score < bestscore) :
                     bestscore = score
        return bestscore



def index(row ,col) :
  
  if row== 0 and col==0 :
     return 1
  
  elif row ==0 and col ==1 :
      return 2
  
  elif row ==0 and col ==2 :
      return 3
  
  elif row ==1 and col ==0 :
      return 4
  
  elif row ==1 and col ==1 :
      return 5
  
  elif row ==1 and col ==2 :
      return 6
  
  elif row ==2 and col ==0 :
      return 7
  
  elif row ==2 and col ==1 :
      return 8
  
  elif row ==2 and col ==2 :
      return 9

def point(move) :
     rows=-1
     cols=-1
     if move==1:
       rows= 0
       cols = 0
     elif move == 2:
       rows= 0
       cols=1
     elif move == 3:
       rows=0
       cols=2
     elif move == 4:
       rows=1
       cols=0
     elif move == 5:
       rows=1
       cols=1
     elif move == 6:
       rows=1
       cols=2
     elif move == 7:
       rows=2
       cols=0
     elif move == 8:
       rows=2
       cols=1
     elif move == 9:
       rows=2
       cols=2

     return rows,cols


def turnplayer(row, column):
  global player
  global buttons
#   print("Its human turn")


  if buttons[row][column]['text']==""  and check_color_winner(player) is False:
     
         buttons[row][column]['text']=player
         move=index(row,column)
         board[move] = player
        #  print(board)

         if check_color_winner(player) is True :
             label.config(text=(player + " won"))

         elif check_color_winner(player) is False :
           player=players[0]
           label.config(text=(player+" turns"))
           turnbot()

         elif empty_spaces() is False :
             label.config(text=("Theres Tie"))

        
def turnbot() :
   global player
   global buttons
   global board

   bestmove = 0
   bestscore = -1000
   for key in board.keys() :
       if (board[key] == ' '):
           board[key] = bot
           score = minimax(board,0,False)
           board[key]= ' '
           if(score> bestscore) :
               bestscore = score
               bestmove = key



    # {1:' ',2:' ',3:' ',
    #    4:' ',5:' ',6:' ',
    #    7:' ',8:' ',9:' '}  

   row,col = point(bestmove)
   buttons[row][col]['text']=bot
   move=index(row,col)
   board[move]=bot
#    print(board)

   if check_color_winner(player) is True :
        label.config(text=(player + " won"))

   elif check_color_winner(player) is False :
           player=players[1]
           label.config(text=(player+" turns"))
          
   elif empty_spaces() is False :
        label.config(text=("Theres Tie"))


def checkwinletter(letter):
    if (board[1]==board[2]==board[3] ) and (board[1] == letter ) :
        return True
    
    elif(board[4]==board[5]==board[6]) and (board[4] == letter) :
        return True
    
    elif(board[7]==board[8]==board[9]) and (board[7] == letter  ):
        return True 
    
    elif(board[1]==board[4]==board[7]) and (board[1] == letter ):
        return True
    
    elif(board[2]==board[5]==board[8]) and (board[2] == letter)  :
        return True
    elif(board[3]==board[6]==board[9]) and (board[3] == letter):
        return True
    
    elif(board[1]==board[5]==board[9]) and (board[1] == letter) :
        return True
    elif(board[3]==board[5]==board[7]) and (board[3] == letter)  :
        return True
    else:
        return False


def check_color_winner(letter):

    for row in range(3):
        if ( buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != ""):

            if (buttons[row][0]["text"]== buttons[row][1]["text"]== buttons[row][2]["text"] == letter ):

                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True

    for col in range(3):
        if (
            buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
            != ""
        ):
            if (
                buttons[0][col]["text"]
                == buttons[1][col]["text"]
                == buttons[2][col]["text"]
                == letter
            ):
                buttons[0][col].config(bg="green")
                buttons[1][col].config(bg="green")
                buttons[2][col].config(bg="green")
                return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        if (
            buttons[0][0]["text"]
            == buttons[1][1]["text"]
            == buttons[2][2]["text"]
            == letter
        ):
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        if (
            buttons[0][2]["text"]
            == buttons[1][1]["text"]
            == buttons[2][0]["text"]
            == letter
        ):
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "tie"

    else:
        return False

    
def checkdraw():
    for key in board.keys() :
       if(board[key] == ' '):
           return False
        
    return True


def empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def turn(row,col):
    #  X-0,Y-1
 
    if player==players[1]:
        turnplayer(row,col)

    elif player==players[0]:
        print("No its me")
        turnbot()


def new_game():
    global player
    global board
    player = random.choice(players)
    label.config(text=player + " turns")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")

    for key in board.keys() :
        board[key] =' '
 

    if(player==players[0]):
     turnbot()



window = Tk()

players = ["X","O"]

bot = "X"
human = "O"
player = random.choice(players)
# player=players[1]



buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
board={1:' ',2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}


label = Label(text=player + " turns", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=("consolas", 40),
            width=5,
            height=2,
            command=lambda row=row, column=column: turn(row, column),
        )

        buttons[row][column].grid(row=row, column=column)

if(player==players[0]):
    turnbot()

window.mainloop()




