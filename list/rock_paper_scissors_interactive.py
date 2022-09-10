import random
from tkinter import * 

dict = {
    "Rock": {"Rock": 1,"Paper": 0,"Scissors": 2},
    
    "Paper":{"Rock": 2,"Paper": 1,"Scissors": 0},
    
    "Scissors":{"Rock": 0,"Paper": 2,"Scissors": 1},
}


comp_score = 0 
user_score = 0

def outcome_handler(user_choice):
    global comp_score
    global user_score
    
    outcomes = ["Rock","Paper","Scissors"]
    random_number = random.randint(0,2)
    computer_choice = outcomes[random_number]
    result = dict[user_choice][computer_choice]
    
    player_choice_label.config(fg = "red",text="player's choice : " +str(user_choice))
    computer_choice_label.config(fg = "blue" , text="computer's choice : " + str(computer_choice))
    
    if result == 2:
        user_score = user_score + 2
        player_score_label.config(font="green",text="player :" +str(user_score))
        outcome_label.config(fg="green",text="player won!!")   
    
    if result == 1:
        user_score = user_score + 1
        comp_score = comp_score + 1
        computer_score_label.config(font="blue",text="computer :" +str(comp_score))
        player_score_label.config(font="green",text="player :" +str(user_score))
        outcome_label.config(fg="blue",text="draw")   
        
    if result == 0:
        comp_score = comp_score + 2
        computer_score_label.config(font="blue",text="computer :" +str(comp_score))
        outcome_label.config(fg="red",text="player lost!!")   

master = Tk()
master.geometry("950x500")
icon = PhotoImage(file = "ICON.png")
master.title("RPS")
master.iconphoto(True,icon)
master.config(background="black")


masterlabel = Label(master,
                    text="ROCK, PAPER, SCISSORS!!",
                    font=("Colic Sans",30),
                    fg="green",
                    bg="black",
                    )
masterlabel.grid(
                row=0,
                sticky = N,
                pady= 10,
                padx=200
                    )

masterlabel2 = Label(master,
                     text="please select an option",
                     font=("Colic Sans",30),
                     fg="green",
                     bg="black"
                    )
masterlabel2.grid(
                    row=1,
                    sticky = N,
                    )
                    
player_score_label = Label(master,
                           text="Player : 0",
                           font=("Colic Sans",12),
                           fg="green",
                           bg="black",
                           )
player_score_label.grid(row=2,sticky=W)

computer_score_label = Label(master,
                           text="computer : 0",
                           font=("Colic Sans",12),
                           fg="green",
                           bg="black",
                           )
computer_score_label.grid(row=2,sticky=E)

player_choice_label = Label(master,
                            font=("calibri",12)
                            )
player_choice_label.grid(row=3,sticky=W)

computer_choice_label = Label(master,
                            font=("calibri",12)
                            )
computer_choice_label.grid(row=3,sticky=E)

outcome_label = Label(master,
                            font=("calibri",20)
                            )
outcome_label.grid(row=3,sticky=N)

       
        
button1 = Button(master,
                text="Rock",
                command= lambda:outcome_handler("Rock"),
                font=("Comic Sans",30),
                fg="red",
                bg="green",
                activeforeground="white",
                activebackground="red",
                )
button1.place(x=300,y=300)


  
    

button2 = Button(master,
                 text = "Paper",
                 font = ("Comic Sans",30),
                 command= lambda:outcome_handler("Paper"),
                 fg="green",
                 bg="red",
                 activeforeground="red",
                 activebackground="white",
                 )
button2.place(x=400,y=200)


button3 = Button(master,
                text="Scissors",
                command= lambda:outcome_handler("Scissors"),
                font=("Comic Sans",30),
                fg="Blue",
                bg="silver",
                activeforeground="silver",
                activebackground="blue",
                )
button3.place(x=500,y=300)



master.mainloop()
