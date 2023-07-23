

import random


print("Welcome to funny name generator!!!\nHope you have fun!!!")
num = int(input("Enter the number of names you have: "))
name = list()

for i in range(num):
    name.append(input("Enter the name : "))


fname_lname = dict([n.split(" ", 1) for n in name])



for fname, lname in fname_lname.items():
    rand_key = random.choice(list(fname_lname.keys()))  
    temp = lname
    fname_lname[fname] = fname_lname[rand_key]
    fname_lname[rand_key] = temp

for k, v in fname_lname.items():
    print(f"{k} {v}")


print("This jumbly name program is developed by Anadi Agrawal. Thanks for using. \nPress ENTER TO EXIT.")
input()
exit()