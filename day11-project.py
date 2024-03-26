#wszystko ponad 10 liczy sie jako 10, as liczy sie jako 1 lub 11 
#Nie mozna przekroczyc 21 
#kto blizej 21 ten wygrywa
#mozna dobra jedna karte 

import random
Wartosc = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10] 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo, '\n')

print('Welcome in the BlackJack!\n')

def losowakarta():
    return Wartosc[random.randint(0 ,13)]

k1 = losowakarta() 
k2 = losowakarta()
cards = [k1, k2]

print(f'Your cards: {cards}, current score = {k1 + k2}')

b1 = losowakarta()
b2 = losowakarta()
botcards = [b1, b2]

print(f'Computer first card: {b1}\n')

stillon = True 
while stillon:
    still = input("Type 'y' to get another card, type 'n' to pass: ")
    if still.lower() == 'n':
        score = k1 + k2
        print(f'\nYour final cards: {cards}. Final score: {score}\n')
        czybotdobiera = random.randint(0,2)
        if czybotdobiera == 1:
            dodatkowabota = losowakarta()
            botcards.append(dodatkowabota)
            botscore = b1 + b2 + dodatkowabota
        else:
            botscore = b1 + b2 
        stillon = False
        print(f"Computer's final cards: {botcards}. Final score: {botscore}\n")
    elif still.lower() == 'y':
        dodatkowa = losowakarta()
        cards.append(dodatkowa)
        stillon = False
        score = k1 + k2 + dodatkowa
        print(f'\nYour final cards: {cards}. Final score: {score}\n')
        czybotdobiera = random.randint(0,2)
        if czybotdobiera == 1:
            dodatkowabota = losowakarta()
            botcards.append(dodatkowabota)
            botscore = b1 + b2 + dodatkowabota
        else:
            botscore = b1 + b2 
        
        print(f"Computer's final cards: {botcards}. Final score: {botscore}\n")

    else:
        print("'Type 'y' or 'n'\n")

if botscore > score:
    print('YOU LOSE\n')
elif score == 21:
    print('!BLACKJACK!\n')
elif score > 21:
    print('YOU LOSE!\n')
else:
    print('YOU WIN\n')