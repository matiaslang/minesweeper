import haravasto, mineService, drawingService, fileService
from os import system, name 

def print_stars():
   for i in range(2):
        for j in range(35):
            print("*", end = '')
        print('')

def ask_numbers(question, error):
    while True:
        try:
            value = int(input(question))
        except ValueError:
            print(error)
        if value <= 0:
            print("Syötä positiivinen luku, joka on suurempi kuin 0\n->")
        else:
            break
    return value

def mineSweeper():
    kentan_x = ask_numbers("Syötä kentän leveys ruuduissa\n->", "Syötä luku joka on suurempi kuin 0.\n->")
    kentan_y = ask_numbers("Syötä kentän korkeus ruuduissa\n->", "Syötä luku joka on suurempi kuin 0.\n->")
    mineQnt = ask_numbers("Syötä miinojen lukumäärä\n->", "Syötä luku joka on suurempi kuin 0.\n->") 
    while mineQnt > (kentan_x * kentan_y - 1):
        print("Syötä miinojen lukumäärä siten, että ne mahtuvat kentälle(Max {} kpl)". format(kentan_x * kentan_y - 1))
        mineQnt = ask_numbers("Syötä miinojen lukumäärä\n->", "Syötä luku joka on suurempi kuin 0.\n->") 
    duration, result, moves = drawingService.main(kentan_x, kentan_y, mineQnt)
    return duration, kentan_x, kentan_y, result, moves

def main():
    clear()
    choice = 0
    print_stars()
    print("  Tervetuloa Miinaharavan pariin")
    print_stars()
    print("\n")
    while True:
        choice = ask_numbers("Valitse seuraavista: \n1. Aloita uusi peli\n2. Katsele tilastoja\n3. Lopeta Ohjelma\n\n->", "Syötä jokin seuraavista: \n        1 | 2 | 3\n->")
        while choice > 4 or choice <= 0:
                print("Syötä jokin seuraavista: \n        1 | 2 | 3")  
                choice = ask_numbers("Valitse seuraavista: \n1. Aloita uusi peli\n2. Katsele tilastoja\n3. Lopeta Ohjelma\n\n->", "Syötä jokin seuraavista: \n        1 | 2 | 3\n->")
        if choice == 1:
            duration, kentan_x, kentan_y, result, moves = mineSweeper()
            fileService.writeRecords(duration, kentan_x, kentan_y, result, moves)
        elif choice == 2:
            fileService.readRecords()
        else:
            print("Selvä homma, pelaillaan joskus toiste! :) ")
            break

        
    #drawingService.main()
    
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
    

if __name__ == "__main__":
    main()
