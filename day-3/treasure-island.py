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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_  
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
*******************************************************************************
''')

print(" Welcome to Lost Relic Quest!")
print("Your goal: Survive the jungle and uncover the hidden treasure.")

first_move = input("You're at a jungle fork. Do you go 'left' or 'right'?\n").lower()

if first_move == "left":
    second_move = input("You reach a wide river. Will you 'wait' for help or 'swim' across?\n").lower()
    if second_move == "wait":
        third_move = input("A raft arrives and you cross safely. On the other side, there's a cave with 3 glowing entrances: one red, one blue, one green. Which do you enter?\n").lower()
        if third_move == "red":
            print(" The room erupts in flames. You're toast. Game Over.")
        elif third_move == "blue":
            print(" Venomous snakes drop from the ceiling. Game Over.")
        elif third_move == "green":
            print(" You found the hidden relic chamber. You win!")
        else:
            print("That's not a valid entrance. You walk into a trap. Game Over.")
    else:
        print(" You get pulled under by something... not friendly. Game Over.")
else:
    print(" You fall into a hidden pit of spikes. Game Over.")
