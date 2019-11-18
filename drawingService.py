import haravasto
import mineService
import time

"""
File that creates the minesweeper game.
creates a dictionary which includes all the essential values for the game to run
@param board: field which consist of n*n of arrays(for example board with size of 2 by 2
starts with [[' ',' '][' ',' ']]), and then gets filled with mines('X')
@param time: duration of the game in seconds
@parm end: parameter indicating if the game has ended or not. 0 = game is going, 1 = game has ended
@param result: 3 = game is going, 1 = win, 0 = lose
@param timeOut: timer to time out after game has ended
@param moves: amount of moves done
"""

tila = {
    "board": None,
    "time": 0,
    "end": 0,
    "result": 3,
    "available" : 9,
    "timeOut": 0,
    "moves": 0
}

SQSIZE = 40

def checkAvailableSpots():
    """
    function to return the amount of squares that has not been opened yet
    @params: None
    @return: the amount of squares with value ' '(square has not been opened yet)
    """
    sum = 0
    for i in tila["board"]:
        sum = i.count(' ') + sum
    return sum

def checkSquare(x,y):
    """
    Function to be excecuted everytime player opens up a square. If clicked square is a bomb,
    game finishes. If it is empty (' ') game continues and board opens up a bit accordingly

    @param x: location of the clicked square on x axel
    @param y: location of the clicked square on y axel
    """

    if tila["board"][y][x] == 'x':
        tila["end"] = 1
        tila["result"] = 0
        loseGame() 
    elif tila["board"][y][x] == ' ':
        if mineService.laske_ninjat(x, y, tila["board"]) > 0:
            tila["board"][y][x] = mineService.laske_ninjat(x, y, tila["board"])
        else:
            tila["board"] = mineService.tulvataytto(tila["board"], x, y)

    tila["available"] = checkAvailableSpots()
    if tila["available"] == 0:
        tila["end"] = 1
        tila["result"] = 1
        winGame()
    tila["moves"] += 1

def loseGame():
    """
    Just prints the given text to clarify that player lost
    """
    teksti = "BOOM, hävisit pelin. Odota muutama sekunti, ja kokeile joskus uudestaan!"
    print(teksti)

def winGame():
    """
    Just prints the given text to clarify that player won the game
    """
    print("Mahtavaa, olette voittaneet pelin! Hienosti tehty :)\n Odota muutama sekunti niin palaat alkuvalikkoon.")

def timeCounter(t):
    """
    Counter function to keep on track of time for the game, and timeout in case game ends.
    """
    tila["time"] = tila["time"] + t
    if tila["end"] == 1:
        tila["timeOut"] = tila["timeOut"] + t
    if tila["timeOut"] > 3:
        haravasto.lopeta()   

def handleClick(x, y, button, modKey):
    """
    Helper function to handle the clicks. If player clicks with mousebutton 1 on the board
    game responds accordingly.
    """
    x_coord = int(x / SQSIZE)
    y_coord = int(y / SQSIZE)
    if button == 1:
        checkSquare(x_coord, y_coord)
        draw_board()
    if button == 4:
        haravasto.lopeta()

def game():
    """
    Function to start the game and start timer and make sure mouse input is taken
    """
    haravasto.aseta_hiiri_kasittelija(handleClick)
    haravasto.aseta_toistuva_kasittelija(timeCounter, 1/60)
    haravasto.aloita()
    

def draw_board():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.aloita_ruutujen_piirto()
    i, j = 0, 0
    while i < len(tila["board"][0]):
        j = 0
        while j < len(tila["board"]):
            if tila["board"][j][i] == " " or tila["board"][j][i] == "x":
                haravasto.lisaa_piirrettava_ruutu(" ", i * SQSIZE, j * SQSIZE)
            elif tila["board"][j][i] >= 0:
                haravasto.lisaa_piirrettava_ruutu(tila["board"][j][i], i * SQSIZE, j * SQSIZE)
            j = j + 1
        i = i + 1

    if tila["result"] == 0:
        i,j = 0,0
        while i < len(tila["board"][0]):
            j = 0
            while j < len(tila["board"]):
                if tila["board"][j][i] == "x":
                    haravasto.lisaa_piirrettava_ruutu("x", i * SQSIZE, j * SQSIZE)
                j = j + 1
            i = i + 1

    if tila["result"] == 1:
        i,j = 0,0
        while i < len(tila["board"][0]):
            j = 0
            while j < len(tila["board"]):
                if tila["board"][j][i] == "x":
                    haravasto.lisaa_piirrettava_ruutu("f", i * SQSIZE, j * SQSIZE)
                j = j + 1
            i = i + 1
    haravasto.piirra_ruudut()
    

def main(width, height, mineQnt):
    """
    main function to start the game. Loads the pictures from given folder and draws wanted
    squares.

    creates an empty table with given height and width, and after that adds random amount
    of mines on given table.

    @param width: width of the board game is played on
    @param height: height of the board game is played on
    @param mineQnt: quantity of mines in game.
    """
    clearTable()
    haravasto.lataa_kuvat("./spritet")
    board = []
    for rivi in range(height):
        board.append([])
        for sarake in range(width): 
            board[-1].append(" ")
    tila["board"] = board
    
    jaljella = []
    for x in range(height):
        for y in range(width):
            jaljella.append((x, y))
            
    mineService.miinoita(tila["board"], jaljella, mineQnt) 
    haravasto.luo_ikkuna(width * SQSIZE, height * SQSIZE)
    haravasto.piirra_tausta()
    haravasto.aseta_piirto_kasittelija(draw_board)
    game()
    return(tila["time"] - 3, tila["result"], tila["moves"])

def clearTable():
    """
    resets the game dictionary to be on default values
    """
    tila["board"] = None
    tila["time"] = 0
    tila["end"] = 0
    tila["result"] = 3
    tila["available"] = 9
    tila["timeOut"] = 0
    tila["moves"] = 0


