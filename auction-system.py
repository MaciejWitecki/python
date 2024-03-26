logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os
os.system('clear')
print(logo, '\nWelcome to the secret auction program.')
name = input('What is your name: ')
bid = input("What's your bid?: ")
while not bid.isdigit():
    print('Give a price.')
    bid = input("What's your bid?: ")

players = {}

stillonbid = True 
winner = ''
max = 0 
while stillonbid: 
    players[name] = bid
    users = input('Are there other users who want to bid? ')
    if users.lower() == 'yes':
        os.system('clear')
        name = input('What is your name: ')
        bid = input("What's your bid?: ")
        while not bid.isdigit():
            print('Give a price.')
            bid = input("What's your bid?: ")
    elif users.lower() == 'no':
        for key in players:
            if max < int(players[key]):
                winner = key
                max = int(players[key])
        stillonbid = False
    else:
        print('Write Yes or No')
os.system('clear')
print(f'The winner is {winner} with a bid of {players[winner]}$.')
