print("Welcome to the game")
adventure = input("do you want to play? ")

if adventure.lower() == "no":
    print("goodbye")
    quit()
else:    
      name = input("Type your name :  ")
      print("Welcome", name, "to this adventure!!")
      print("If you take the blue pill you'll be in charge of the digital project 'code_blue' but if you choose the red one you'll go through a journey to invent a time machine ") 
      choice = input("so... What's your choice? ")    
      if choice == "blue pill":
         print("OK, but be cautious with your steps before you get destroyed by them")
         print("In 1956, the US governement decided to test its cababilities in the world of machine code, to this end they have established the Advanced Machine Coding Hub (AMCH), and with the came up with various projects, one of which was code blue ")
         print("You are a head of staff for the company, let's go.")
         decision = input("Michael: Hello Mr " + name + ",good to see you here, we're testing a new program called 'code blue', it is a program that will enable humanized robots to do dangerous, repetitive, or boring tasks, oh man, we are going to get a multi million dollars deal with anyone, but first I need to ask you something, who should we deal with? the army, the governement or the zindax, honestly, I prefer the last option, but what do you think?(answer with typing one of the names) ")
         if input.lower() == "the army":
           print("ok, but we have to talk with general James about this")
           print("Later...")
           print("Gen.James: hello there , nice to meet the people from that company that I don't understand its functions yet, what do you have for")
           print("Michael: Gen.James, I appreciate the welcoming, me and Mr",name,"have a project to replace bomb guys with our own robots")
           print("Gen.James: I see that, what is the deal? I'm offering 20 Million$")
           input("Michael: what do you think chief? accept or not")
           if input.lower() != "yes":
             print("Gen.James: I guess your time is up, boys, ELIMINATE!!!!")
             print("GAME OVER!")
             quit()
             
           else : 
             print("Gen.James: we're on the same page then huh??")
             print("And now you've just allign your comapny to the army...")
             print("But the general betrayed you !!!")
             print("GAME OVER!!")
             quit()
         
         elif input.lower() == "the governemet" :
           print("Michael: let's call president Harry about this")
           print("Later...")
           print("Michael: hello Mr President, it is the company's honour to present to you 'code_blue',I believe you do know what it is President Harry")
           print("President: yes, I know the important value of the project, so we offer you a 10 million$ price tag")
           input("Michael: what do you think chief? accept or not")
           if input.lower() == "yes":
             print("Michael: I guess it's a deal Mr President.")
             print("President: excellent")
             print("now you've established your company to become one of the finest of the entire US scientific hub ")
           
      elif choice =="red pill":
        print()
    
      else:
        print("restart")
        quit()
        