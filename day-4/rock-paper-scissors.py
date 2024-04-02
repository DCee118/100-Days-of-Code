import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input('What do you choose? \n0 for Rocks \n1 for Paper \n2 for Scissors \n'))
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
    
computer_choice = random.randint(0,2)
print('Computer chose:')
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors) 

if player_choice >= 3 or player_choice < 0:
    print('Invalid chose! You lose!')
elif player_choice == 1 and computer_choice == 0:
    print('You win!')
elif player_choice == 2 and computer_choice == 1:
    print('You win!')
elif player_choice == computer_choice:
    print('Draw')
elif player_choice == 0 and computer_choice == 2:
    print('You win!')
else:
    print('You lose! :(')