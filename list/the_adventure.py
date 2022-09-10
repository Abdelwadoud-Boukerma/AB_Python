from distutils.util import copydir_run_2to3
from tkinter import *
import random
options = ["rock","paper","scissors"]
user_wins = 0
computer_wins = 0
random_number = random.randint(0,2)
#rock is 0 paper is 1 scissors is 2
computer_pick = options[random_number]
print("Computer picked" , computer_pick + ".")
# widgets = GUI components : buttons , textboxes , images , labels
# window = a container for the widgets
count = 0
countb = 0
countc = 0
window = Tk() # instantiates an instance of a window
window.geometry("1050x1050") # sets the size of the window 
window.title("Rock paper scissors!!")
icon = PhotoImage(file = "1200px-python-logo-notext.svg.png")#photo of the icon
window.iconphoto(True,icon)#display the icon
window.config(background="black")#backrgound color

photo = PhotoImage(file ="Visual_Studio_Code_1.35_icon.svg.png")


  

label = Label(window,
              text = "ROCK, PAPER, SCISSORS!!",
              font=("arial" ,40 ,"italic"),
              fg="#66CD00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              #image=photo,
              )

def click():
   print("hello")
       
        
button1 = Button(window,
                text="Rock",
                command=click,
                font=("Comic Sans",30),
                fg="red",
                bg="green",
                activeforeground="white",
                activebackground="red",
                )
button1.place(x=300,y=300)

def click2():
    print("rock")
  
    

button2 = Button(window,
                 text = "Paper",
                 font = ("Comic Sans",30),
                 command= click2,
                 fg="green",
                 bg="red",
                 activeforeground="red",
                 activebackground="white",
                 )
button2.place(x=400,y=200)

def click3():
   print("hello")

button3 = Button(window,
                text="Scissors",
                command=click3,
                font=("Comic Sans",30),
                fg="Blue",
                bg="silver",
                activeforeground="silver",
                activebackground="blue",
                )
button3.place(x=500,y=300)


player_score_label = Label(window,
                        text="PLayer : 0",
                        font=("Comic Sans",20),
                        fg="green",
                           )
player_score_label.place(x=0,y=1000)


               




label.pack()
#label.place(x=0,y=0)

     

window.mainloop() # display a window on the screen, listen for events