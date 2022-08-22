# Imagem importada de ASCII Art
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("Welcome to Treasure Island!\nYour mission is to find the the ONE PIECE!!!")
first = input("You are navigating in the New Wolrd! You can see two isles, wich one you want to go? Type 'left' of 'right': ").lower()
if first == "left":
    second = input("The island is beautiful! Walking by the sand you find a misterius cave. Inside the cave there is a lake. Do you want to swin across or get a boat? Type 'swin' or 'boat': ").lower
    if second == "boat":
        terceira = input("Great! After a walk inside the cave you see 3 routes, one right with a Red door, one northwest with a Yellow door, and the last one at the southwest with a Blue door. Wich one will you choose? Type 'red', 'yellow' or 'blue': ").lower()
        if terceira == "red":
            print("Wrong door fool! A giant demon covered by flames look ate you in the eyes and before you could run out, he pull your soul of your body and traps inside a bottle! Game over.")
        elif terceira == "yellow":
            print("Great! You find the precious ONE PIECE!!! You barely can see the ende of the cave, covered by all the treasures that you can find in the world! Go on and call your tripulation!")
        elif terceira == "blue":
            print("Bad choice! A trap is activated and you get a shot of a poison dart right into your chest. That's a bad way to die. Game over.")
        else:
            print("(INCORRECT KEY)Without a choise, you stay there into the cave waiting eternaly until a ghost appear and scares you. When you wake up, all the doors have gone. Game over.")
    elif second == "swin":
        print("Bad choice folk. You start to fell heavy and more heavy! You look down and you can't the the botton of the lake. That's the end of your jorney.")
    else:
        print("(INCORRECT KEY) You just decided to not enter the cave and go back to your ship.")        
elif first == "right":
    print("You choose the wrong island! It was a giant turtle that eats your ship!\nGame Over for you.")
else:
    print("(INCORRECT KEY!) None of the islands have been decided. Instead, you just find a strange barrel on the sea. When you catch it, a strange firework go out of the barrel and the sky start to go dark.")