import random

print("Welcome to this next game")
print("in it you can guess the number ")

top_of_range = input("Type a number between 0 and 100: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range >=0 and top_of_range <=100:
       random_number = random.randint(0,100)
       print(random_number)
       if top_of_range == random_number:
           print("good job")
    
    else:
       print("next time type a number between 0 and 100")
       quit()
else:
    print("please type a number")
    quit()