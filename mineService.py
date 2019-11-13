import random
import main

def laske_ninjat(x, y, lista):
    """
    Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole ninjaa - jos on, sekin lasketaan mukaan.
    """
    ninjat = 0
    leveys = len(lista[1])
    korkeus = len(lista)
    a_x = x - 1
    a_y = y - 1

    for i in range(3):
        if a_y >= 0 and a_y < korkeus:
            for j in range(3):
                if a_x >= 0 and a_x < leveys:
                    if lista[a_y][a_x] == 'x':
                        ninjat += 1
                a_x += 1
        a_x = x - 1
        a_y += 1

    return ninjat

def tulvataytto(planeetta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    leveys = len(planeetta[1])
    korkeus = len(planeetta)
    lista = [(x, y)]
    i = 0
    flag = 1
    while flag:
        numero = lista.pop(-1)
        a_x = numero[0] - 1
        a_y = numero[1] - 1 
        for i in range(3):
            if a_y >= 0 and a_y < korkeus:
                for j in range(3):
                    if a_x >= 0 and a_x < leveys:
                        if planeetta[a_y][a_x] == ' ':
                            minesNextTo = laske_ninjat(a_x, a_y, planeetta)
                            planeetta[a_y][a_x] = minesNextTo
                            numToAdd = (a_x, a_y)
                            lista.append(numToAdd)
                        if planeetta[a_y][a_x] == 'x' or len(lista) == 0:
                            flag = 0
                    a_x += 1
            a_x = numero[0] - 1
            a_y += 1
    return planeetta
        


def miinoita(kentta, availableSpots, mineQt):
    """
    Asettaa kentällä N kpl miinoja satunnaisiin paikkoihin.
    """
    for i in range(mineQt):
        value = random.choice(availableSpots)
        availableSpots.remove(value)
        kentta[value[0]][value[1]] = 'x'

    return kentta
   