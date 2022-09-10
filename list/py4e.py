user_input= input('Please enter your name sir ')
print("welcome", user_input)


print("Enter hours:")

hours= input()

print("Enter rate:")

rate= input()
try:
    if int(hours) > 40:
        def pay():
            res= float(hours) * (float(rate) * 1.5)
            return res 
        print("Pay:", pay())
    else:
        def pay():
            res= float(hours) * (float(rate) * 1.5)
            return res 
        print("Pay:", pay())
    if pay()< 20:
        print("bad")
    print("good")
except:
    print("retry sir")

print("done")

str = "X-DSPAM-Confidence: 0.8475"

colon = str.find(":")
print(colon)



info = str[colon+ 1: ]

print(float(info))


