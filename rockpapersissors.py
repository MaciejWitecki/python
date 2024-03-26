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


import random 
end = 0
while end == 0:
    player = ''
    while player == '':
        player = input('\nRock, paper or scissors?\n').lower().strip()
        if player == 'rock' or player =='paper' or player == 'scissors':
            continue
        else:
            player = ''
            print('\nWrong option!\n')

    computer = random.randint(1,3)

    if player == 'rock':
        player = 1
        print(rock)
    elif player == 'paper':
        player = 2
        print(paper)
    else:
        player = 3
        print(scissors)


    if player == 1 and computer == 2: 
        print(f'Computer choose:\n{paper}\nYou lose!\n')
        end = 1 
    elif player == 1 and computer == 1:
        print(f'Computer choose:\n{rock}\nOne more time!\n')
    elif player == 1 and computer == 3:
        print(f'Computer choose:\n{scissors}\nYou win!\n')
        end = 1
    elif player == 2 and computer == 1:
        print(f'Computer choose:\n{rock}\nYou Win!\n')
        end = 1
    elif player == 2 and computer == 2:
        print(f'Computer choose:\n{paper}\nOne more time!\n')
    elif player == 2 and computer == 3:
        print(f'Computer choose:\n{scissors}\nYou lose!\n')
        end = 1
    elif player == 3 and computer == 1:
        print(f'Computer choose:\n{rock}\nYou lose!\n')
        end = 1
    elif player == 3 and computer == 2:
        print(f'Computer choose:\n{paper}\nYou win!\n')
        end = 1
    elif player == 3 and computer == 3:
        print(f'Computer choose:\n{scissors}\nOne more time!\n')
