import random

def zadanie1():
    stany = []
    for i in range(1, 7):
        stany.append([0,0])

    model = ['S', ' ', ' ',' ',' ', 'G']
    alfa = 0.1
    gamma = 0.9

    for i in range(100):
        r = 0
        pozycja = 0
        ruch = [0, 1]
        poprzednia_pozycja = pozycja

        for proba in range(1, 100):
            poprzednia_pozycja = pozycja
            gdzie_isc = random.choice(ruch)
            if (gdzie_isc == 0):
                pozycja -= 1
                if (pozycja < 0):
                    pozycja = 0

            else:
                pozycja += 1

            if (model[pozycja] == 'G'):
                r = 1
            stany[poprzednia_pozycja][gdzie_isc] = round(stany[poprzednia_pozycja][gdzie_isc] + alfa * (r + gamma * max(stany[pozycja]) - stany[poprzednia_pozycja][gdzie_isc]), 3)
            if (r == 1):  break
    for row in stany:
        print(row)




if __name__ == '__main__':
    zadanie1()

