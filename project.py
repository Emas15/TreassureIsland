print('''
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
/______/______/______/______/______/______/______/______/______/______/_____
*******************************************************************************
      ''')
#by using 3 single quote i prints line by line

print("Welcome to the Treasure Island. Your mission is to find the treasure\n")

start = input('You\'re at the entry point! Where do you want to go? Type "left" or "right". \n').lower()


if start == 'left':
    choice1 = input("You\'ve come to a lake. There is a island in the middle of the lake, Type 'wait' for a boar. Type 'swim' to swim across . \n").lower()
    if choice1 == 'wait':
       choice2 = input("You arrived at the island Gigaland. There is a house with 3 doors. One red, one yellow and one blue.Which color do you choose? \n").lower()
       if choice2 == 'red':
           print("It's a room full of fire. Game over!")
       elif choice2 == 'yellow':
           print('There was a hungry lion in that room! Game over!')
       elif choice2 == 'blue':
           print('You found the treasure! You win!!!')
       else:
           print("you chose a door that does not exist. game over!")
    
    else:
        print('There was a crocodile in the river! Game over!')
else:
    print("You fell into a trap! Game over!")
