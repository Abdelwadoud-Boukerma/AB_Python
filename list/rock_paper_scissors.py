import random
options = ["rock","paper","scissors"]
user_wins = 0
computer_wins = 0

while True :
    user_input = input("Rock , paper or scissors or type Q to quit.").lower()
    if user_input == "q":
        break
    if user_input not in options:
       continue
    random_number = random.randint(0,2)
    #rock is 0 paper is 1 scissors is 2
    computer_pick = options[random_number]
    print("Computer picked" , computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("you won!!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!!")    
        user_wins += 1 
    
    elif user_input == "paper" and computer_pick == "paper":
        print("draw")
    
    elif user_input == "rock" and computer_pick == "rock":
        print("draw")
        
    elif user_input == "scissors" and computer_pick == "scissors":
        print("draw")
         
    else : 
       print("you lost")
       computer_wins += 1 
print("you won", user_wins, "times")
print("the computer won", computer_wins , "times")
print("Goodbye!!")