# SNAKE WATER GUN GAME

import random
import os

col , lin = os.get_terminal_size()


def swg():
    print(("INSTRUCTIONS:").center(col))
    print(("YOU WILL BE GIVEN 10 CHANCES.").center(col))
    print(("YOU HAVE TO SELECT S FOR SNAKE, W FOR WATER AND G FOR GUN").center(col))
    print(("YOU WILL  BE PLAYING ANONYMUSLY WITH COMPUTER").center(col))
    print(("ONCE YOU SELECT THE CHOICE, YOU WILL BE GIVEN IF YOU WON ON THAT CHANCE.").center(col))
    print(("IF YOU WON IN MORE THAN 5 CHANCES. THEN YOU WIN THE MATCH.").center(col))
    input(("PRESS ENTER TO PLAY!!!").center(col))
    cis = ["s", "w", "g"]
    i=1
    nt=0
    uw=0
    cw=0
    while i in range(1,11):
        print("THIS IS YOUR CHANCE NUMBER: ",i )
        b = input("Enter your choice : ")
        a = random.choice(cis)
        print("Computer's choice :",a)
        if a=="s" and b=="s":
            print("IT'S A TIE...")
            nt+=1
        elif a=="s" and b=="w":
            print("YOU LOST!!!")
            cw+=1
        elif a=="s" and b=="g":
            print("YOU WON!!!")
            uw+=1
        elif a=="w" and b=="s":
            print("YOU WON!!!")
            uw+=1
        elif a=="w" and b=="w":
            print("IT'S A TIE...")
            nt+=1
        elif a=="w" and b=="g":
            print("YOU LOST!!!")
            cw+=1
        elif a=="g" and b=="s":
            print("YOU LOST!!!")
            cw+=1
        elif a=="g" and b=="w":
            print("YOU WON!!!")
            uw+=1
        elif a=="g" and b=="g":
            print("IT'S A TIE...")
            nt+=1
        i+=1
    u=str(uw) 
    c=str(cw)
    print(("GAME ENDED!!!").center(col))
    print(("YOU WON "+u+" NUMBER OF TIME!!!").center(col))
    print(("COMPUTER WON " +c+" NUMBER OF TIMES!!!").center(col))

    if uw>cw:
        print(("HURRAY!!!YOU WON THE MATCH FROM THE COMPUTER!!!").center(col))
        print(("CONGRATULATIONS").center(col))

    elif uw<cw:
        print(("YOU LOST THE MATCH!!!").center(col))
        print(("GAME OVER!!!").center(col))

    else:
        print(("YOU MADE A TIE WITH THE COMPUTER!!").center(col))




print(("THIS IS A SNAKE WATER GUN GAME.").center(col))

swg()

i=input("Do you want to play again??? Y/N : ").capitalize()

if i =="Y":
    swg()

else:
    print(("THIS GAME IS DEVELOPED BY ANADI AGRAWAL...").center(col))
    input(("PRESS ENTER TO EXIT!!!").center(col))
    exit()