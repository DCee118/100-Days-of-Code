import time

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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island!')
time.sleep(1)
print('Your mission is to find the treasure.')
time.sleep(1)
print('You have arived on the island and you walk into the jungle.')
time.sleep(2)
print('It suddenly becomes dark, you reach a dead end.')
time.sleep(2)
left_or_right = input('Do you turn left towards the river or right towards a cave? ')
time.sleep(1)
if left_or_right == 'left':
    print('You walk towards the river and you recognise it has very strong current.')
    time.sleep(2)
    print('Do you swim across the river or wait till the river calms but risk getting attacked by the creatures that come out at night.')
    time.sleep(2)
    swim_or_wait = input('Swim or wait? ')
    if swim_or_wait == 'wait':
        print('You wait till sun rise and cross the river safely.')
        time.sleep(1)
        print('You find an entrance that leads underground.')
        time.sleep(1)
        print('You find 3 doors. Blue, red and yellow door.')
        time.sleep(1)
        door = input('which door do you enter? ')
        if door == 'red':
            print('You have fallen into a fire pit....')
            time.sleep(1)
            print('GAME OVER!')
        elif door == 'blue':
            print('You have been locked in a room with a great beast.....')
            time.sleep(1)
            print('GAME OVER!')
        elif door == 'yellow':
            print('You have found the treasure!')
            time.sleep(1)
            print('YOU WIN!')
        else:
            print('GAME OVER!')
    else:
        print('You attempt to swim across.')
        time.sleep(1)
        print('You have been attacked by trout.')
        time.sleep(1)
        print('GAME OVER!')
else: 
    print('You have fallen into a hole.....')
    time.sleep(1)
    print('GAME OVER!')