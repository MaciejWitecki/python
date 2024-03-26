
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

print('Witaj w kalkulatorze!\n')


dzialanie = True


def dodawanie(a, b):
    return int(a) + int(b)
def odejmowanie(a ,b):
    return int(a) - int(b)
def mnozenie(a , b):
    return int(a) * int(b)
def dzielenie(a, b):
    return int(a) // int(b)
def potega(a, b):
    return int(a) ** 2
def pierwiastek(a, b):
    return int(a) ** 0.5

while dzialanie:
    print('\nWybierz jedna z opcji:\n-dodawanie\n-odejmowanie\n-mnozenie\n-dzielenie\n-potega\n-pierwiastek\n')
    czynnosc = input('Czynnosc: ')
    if czynnosc.lower() == 'dodawanie':
        a = input('Podaj pierwsza liczbe: ')
        b = input('Podaj druga liczba: ')
        if str(a).isdigit() == False:
            print('Podaj liczbe\n')
            a = input('Podaj pierwsza liczbe: ')
        if str(b).isdigit() == False:
            print('Podaj liczbe\n')
            b = input('Podaj druga liczbe: ')
        print(dodawanie(a ,b))
        dalej = input('Czy chcesz cos jeszcze obliczyc? tak/nie\n')
        if dalej.lower() == 'tak':
            continue
        elif dalej.lower() == 'nie':
            break
    elif czynnosc.lower() == 'odejmowanie':
        a = input('Podaj pierwsza liczbe: ')
        b = input('\nPodaj druga liczba: ')
        if str(a).isdigit() == False:
            print('Podaj liczbe\n')
            a = input('Podaj pierwsza liczbe: ')
        if str(b).isdigit() == False:
            print('Podaj liczbe\n')
            b = input('Podaj druga liczbe: ')
        print(odejmowanie(a ,b))
        dalej = input('Czy chcesz cos jeszcze obliczyc? tak/nie\n')
        if dalej.lower() == 'tak':
            continue
        elif dalej.lower() == 'nie':
            break
    elif czynnosc.lower() == 'mnozenie':
        a = input('Podaj pierwsza liczbe: ')
        b = input('\nPodaj druga liczba: ')
        if str(a).isdigit() == False:
            print('Podaj liczbe\n')
            a = input('Podaj pierwsza liczbe: ')
        if str(b).isdigit() == False:
            print('Podaj liczbe\n')
            b = input('Podaj druga liczbe: ')
        print(mnozenie(a ,b))
        dalej = input('Czy chcesz cos jeszcze obliczyc? tak/nie\n')
        if dalej.lower() == 'tak':
            continue
        elif dalej.lower() == 'nie':
            break
    elif czynnosc.lower() == 'dzielenie':
        a = input('Podaj pierwsza liczbe: ')
        b = input('\nPodaj druga liczba: ')
        if str(a).isdigit() == False:
            print('Podaj liczbe\n')
            a = input('Podaj pierwsza liczbe: ')
        if str(b).isdigit() == False:
            print('Podaj liczbe\n')
            b = input('Podaj druga liczbe: ')
        print(dzielenie(a ,b))
        dalej = input('Czy chcesz cos jeszcze obliczyc? tak/nie\n')
        if dalej.lower() == 'tak':
            continue
        elif dalej.lower() == 'nie':
            break
    elif czynnosc.lower() == 'potega':
        a = input('Podaj pierwsza liczbe: ')
        if str(a).isdigit() == False:
            print('Podaj liczbe\n')
            a = input('Podaj pierwsza liczbe: ')
        print(potega(a ,0))
        dalej = input('Czy chcesz cos jeszcze obliczyc? tak/nie\n')
        if dalej.lower() == 'tak':
            continue
        elif dalej.lower() == 'nie':
            break
    elif czynnosc.lower() == 'pierwiastek':
        a = input('Podaj pierwsza liczbe: ')
        if str(a).isdigit() == False:
            print('Podaj liczbe\n')
            a = input('Podaj pierwsza liczbe: ')
        print(pierwiastek(a ,0))
        dalej = input('Czy chcesz cos jeszcze obliczyc? tak/nie\n')
        if dalej.lower() == 'tak':
            continue
        elif dalej.lower() == 'nie':
            break

