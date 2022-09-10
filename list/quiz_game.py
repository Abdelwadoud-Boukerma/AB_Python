print("welcome to the game!")

play = input("Do you want to play? ")

print("The answer: " + play)
 
if play.lower() != "yes":
    quit()

print("Okay , let's play :)")

quiz1 = input("What is the capital of Algeria? ")
score = 0
if quiz1.lower() != "algiers":
    print("False")
    print("The answer is Algiers")
    
if quiz1.lower()== "algiers":
    print("True!! Great job")
    score += 1
    
quiz2 = input("When did Algeria became independent? ")
if quiz2.lower() != "5th of july 1962":
    print("False")
    print("The answer is the 5th of July 1962")
else:
    print("True")    
    score += 1

quiz3 = input("What does the cpu stand for? ")
if quiz3.lower() != "central processing unit":
    print("False")
    print("The answer is 'central processing unit'")
else:
    print("True")
    score += 1    

quiz4 = input("Who is the founder of Apple? ")
if quiz4.lower() != "steve jobs":
    print("False")
    print("The answer is Steve Jobs")
else:
    print("True")
    score += 1
    
quiz5 = input("What is the best programming language to learn? ")
if quiz5.lower() != "python":
    print("False")
    print("The answer is python")
else:
    print("Correct")
    score += 1 

quiz6 = input("Which continent does USA exist on? ")
if quiz6.lower() != "america":
    print("False")
    print("The answer is america")
else:
    print("wonderful")
    score += 1
    
quiz7 = input("what equation is newton most famous for? ")
if quiz7.lower() != "force = mass * acceleration" :
    print("False")
    print("The answer is Force = Mass * Acceleration")
else:
    print("correct")   
    score += 1
    
print("Your score is %i" % score)