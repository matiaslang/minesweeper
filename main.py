import haravasto, mineService, drawingService, fileService
from os import system, name 

"""
Main file for minesweeper function

"""

def print_stars():
    """
    Prints 35 stars in two different rows. Just to make the headline
    look fancier

    @params None
    @return None
    """
    for i in range(2):
            for j in range(35):
                print("*", end = '')
            print('')

def ask_numbers(question, error):
    """
    This function asks user to give a number as an input,
    and validates it to match spesicitations (must be a number and < 0)

    @params question: question to be shown to user
    @params error: error message to be shown if user input is not valid
    @return: return a number value which passes the rules
    """
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
    """
    This function starts the minesweeper game. 
    Game starts by asking size of the gametable and amount of mines, and starts
    the graphical game by those values.

    @params: None
    @returns: duration of the game, size of the table game was played, win/loss(0 = loss 1 = win) and moves it took

    """
    size_x = ask_numbers("Syötä kentän leveys ruuduissa\n->", "Syötä luku joka on suurempi kuin 0.\n->")
    size_y = ask_numbers("Syötä kentän korkeus ruuduissa\n->", "Syötä luku joka on suurempi kuin 0.\n->")
    mineQnt = ask_numbers("Syötä miinojen lukumäärä\n->", "Syötä luku joka on suurempi kuin 0.\n->") 
    while mineQnt > (size_x * size_y - 1):
        print("Syötä miinojen lukumäärä siten, että ne mahtuvat kentälle(Max {} kpl)". format(kentan_x * kentan_y - 1))
        mineQnt = ask_numbers("Syötä miinojen lukumäärä\n->", "Syötä luku joka on suurempi kuin 0.\n->") 
    duration, result, moves = drawingService.main(size_x, size_y, mineQnt)
    return duration, size_x, size_y, result, moves

def main():
    """
    main function to wrap all the functionalities together. First prints the welcome message,
    and then gives a menu of three choices which user can choose from. 1. Start a game,
    2. show results from the previous games and 3. end the application.
    """
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
    """
    function to clear the console screen

    @params: None
    @return: None
    """
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
    

if __name__ == "__main__":
    main()
