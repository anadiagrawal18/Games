#Guess the number GAME
# this game was developed by anadi agrawal

import random 

def conut():
    r = random.randint(a,b)
    print("A random integer has been generated. now fill your guess")
    g = int()
    try:
        i=0
        while g != r:
            g=int(input("ENTER YOUR GUESS : "))
            if g == r:
                print("CONGRATULATIONS!!! YOU GOT THE RIGHT GUESS...")
                print("NUMBER OF GUESSES TOOK TO FINISH",i)
                break
            elif g > r:
                print("WRONG GUESS !!! DECREASE YOUR GUESS.")
                i+=1
            elif g < r:
                print("WRONG GUESS !!! INCREASE YOUR GUESS.")
                i+=1

        return i 
    except Exception as e:
        print(e)
        conut()



print("Welcome to guess the number game")
a = int(input("Enter a number to fix your minimum guess : "))
b = int(input("Enter a number to fix your maximum guess : "))


print("It's chance for player 1")
f = conut()


print("It's chance for player 2")
d = conut()


if f ==d:
    print("It's a tie match")

elif f < d:
    print("""PLAYER 1 WON THE MATCH. 
    CONGRATULATIONS TO PLAYER 1!!!""")

elif f > d:
    print("""PLAYER 2 WON THE MATCH. 
    CONGRATULATIONS TO PLAYER 2!!!""")
    


print("THANKS TO PLAY THE GAME. THIS GAME IS DEVELOPED BY ANADI AGRAWAL...")
print("PRESS ANY KEY TO EXIT!!!")
input()