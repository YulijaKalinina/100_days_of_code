print(r'''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island.\n"
      "Your mission is to find the treasure.")

choice1 = input("You are at cross road. "
                "Where do you want to go?\n      "
                "Type 'left' or 'right'\n").lower()
if choice1 == "left":
    choice2 = input("We've come to a lake. There is an island in the middle of the lake.\n      "
                    "Type 'wait' to wait for a boat. "
                    "Type 'swim' to swim across\n").lower()
    if choice2 == "wait":
        choice3 = input("You have arrived to the island unharmed. "
                        "There is a house with 3 doors. "
                        "Choose the door:\n      Type 'red', 'yellow' or 'blue'\n").lower()
        if choice3 == "yellow":
            print("You Win! You found the treasure!")
        elif choice3 == "red":
            print("You were burned by fire. Game Over.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game Over.")
        else:
            print("Game Over")
    else:
        print("You were attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
