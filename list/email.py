import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input = input("please enter your email: ")

if(re.search(pattern,user_input)):
    print("valid email") 
    
else:
    print("invalid email")

