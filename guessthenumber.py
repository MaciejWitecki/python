logo = """
   ___                     _____  _                 __                    _                 
  / _ \ _   _   ___  ___  /__   \| |__    ___    /\ \ \ _   _  _ __ ___  | |__    ___  _ __ 
 / /_\/| | | | / _ \/ __|   / /\/| '_ \  / _ \  /  \/ /| | | || '_ ` _ \ | '_ \  / _ \| '__|
/ /_\\ | |_| ||  __/\__ \  / /   | | | ||  __/ / /\  / | |_| || | | | | || |_) ||  __/| |   
\____/  \__,_| \___||___/  \/    |_| |_| \___| \_\ \/   \__,_||_| |_| |_||_.__/  \___||_|   
                                                                                           
"""
        
print(logo, '\n')

from random import randint

answer = randint(1, 100)
number_guess = 0; 
# print(answer)
def difficulty(diff):
    global number_guess
    while diff != "easy" and diff != "hard":
        diff = input("Choose a difficulty. Type 'easy' or 'hard': ") 
    if diff == "easy":
        number_guess = 10
    else:
        number_guess = 5

print("Welcome to GuessTheNumber Game!")
print("I'm thinking about number between 1 and 100.\n")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ") 
difficulty(diff)

print(f'\nYou have got {number_guess} chance to win!\n')

def low_high(num, answer):
    if num > answer:
        print("\nToo High!\n")
    else:
        print("\nToo Low\n")
    

while number_guess > 0: 
    guess = int(input("Make a guess: "))  

    if guess == answer:
        print("\nCongrats! You win!\n")
        exit()
    else:
        low_high(guess, answer)
    number_guess -= 1
print("\nYou lose!\n")
print(f'The correnct number is {answer}!\n')