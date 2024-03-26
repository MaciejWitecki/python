print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
                                       ''')

print('Welcome to Treasure Island.\nYour mission is to find the treasure.\n')

where = ''
while where == '':
    where = input('Where do you want to go?\n     LEFT | RIGHT\n').lower()
    if where == 'right' or where == 'left':
        continue
    else:
        print("\nYou can't go there!\n")
        where = ''

if where == 'right':
    print("\nGAME OVER \nFall into a hole.")

else:
    how = ''
    while how == '':
        how = input('What do you want to do now?\n     WAIT | SWIM\n').lower()
        if how == 'swim' or how == 'wait':
         continue
        else:
            print("\nChoose one option!\n")
            how = ''
    if how == 'swim':
        print('\nGAME OVER\nAttacked by trout.')
    else:
        end = input('Which door?\n').lower()
        if end == "red":
            print("\nBurned by fire.\nGAME OVER")
        elif end == 'yellow':
            print("\nYOU WIN")
        elif end == 'blue':
            print('\nEaten by beasts.\nGAME OVER')
        else:
            print('\nWrong answer.\n GAME OVER')         
