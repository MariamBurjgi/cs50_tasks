name = input("What is your name? ")
namelen = len(name)

if namelen <= 3:
    print("Hi, " + name + ", hello there!")
elif namelen <7>3:
    print("Hello, " + name + ", nice to meet you, darling!")
elif namelen ==7:
    print("Hi, " + name + ", try again")
else:
    print("You are welcome,  " + name + ", your name is long!")