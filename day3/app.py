#treasure island

logo = '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print(logo)
print('Welcome to treasure island, your mission to find treasure')
left_or_right = input('You are in Cave, Do you want to go left or right? ').lower()
if left_or_right == 'right':
    print('you fell in hole, Game over!')
else:
    decision = input('you move forward you see a lake do you want to swim or wait? ').lower()
    if decision == 'swim':
        print('you eaten by crocdile, Game over!')
    else:
        door = input('you catched the boat and crossed over the river, you see 3 door, red, blue, yellow, which door '
                     'you want to choose: ').lower()
        if door == 'red':
            print('you burned by fire. Game over!')
        elif door == 'blue':
            print('you eaten by beast, Game over!')
        elif door == 'yellow':
            print('you found treasure, You win')
        else:
            print("please enter valid input")