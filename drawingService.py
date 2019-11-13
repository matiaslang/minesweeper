import haravasto
import mineService
import time

tila = {
    "kentta": None,
    "time": 0,
    "end": 0,
    "result": 3,
    "available" : 9,
    "timeOut": 0,
    "moves": 0
}

SQSIZE = 40

def checkAvailableSpots():
    sum = 0
    for i in tila["kentta"]:
        sum = i.count(' ') + sum
    return sum

def checkSquare(x,y):
    if tila["kentta"][y][x] == 'x':
        tila["end"] = 1
        tila["result"] = 0
        loseGame() 
    elif tila["kentta"][y][x] == ' ':
        if mineService.laske_ninjat(x, y, tila["kentta"]) > 0:
            tila["kentta"][y][x] = mineService.laske_ninjat(x, y, tila["kentta"])
        else:
            tila["kentta"] = mineService.tulvataytto(tila["kentta"], x, y)

    tila["available"] = checkAvailableSpots()
    if tila["available"] == 0:
        tila["end"] = 1
        tila["result"] = 1
        winGame()
    tila["moves"] += 1

def loseGame():
    teksti = "BOOM, hävisit pelin. Odota muutama sekunti, ja kokeile joskus uudestaan!"
    print(teksti)

def winGame():
    print("Mahtavaa, olette voittaneet pelin! Hienosti tehty :)\n Odota muutama sekunti niin palaat alkuvalikkoon.")

def timeCounter(t):
    tila["time"] = tila["time"] + t
    if tila["end"] == 1:
        tila["timeOut"] = tila["timeOut"] + t
    if tila["timeOut"] > 3:
        haravasto.lopeta()   

def handleClick(x, y, button, modKey):
    x_coord = int(x / SQSIZE)
    y_coord = int(y / SQSIZE)
    if button == 1:
        checkSquare(x_coord, y_coord)
        piirra_kentta()
    if button == 4:
        haravasto.lopeta()

def game():
    haravasto.aseta_hiiri_kasittelija(handleClick)
    haravasto.aseta_toistuva_kasittelija(timeCounter, 1/60)
    haravasto.aloita()
    

def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.aloita_ruutujen_piirto()
    i, j = 0, 0
    while i < len(tila["kentta"][0]):
        j = 0
        while j < len(tila["kentta"]):
            if tila["kentta"][j][i] == " " or tila["kentta"][j][i] == "x":
                haravasto.lisaa_piirrettava_ruutu(" ", i * SQSIZE, j * SQSIZE)
            elif tila["kentta"][j][i] >= 0:
                haravasto.lisaa_piirrettava_ruutu(tila["kentta"][j][i], i * SQSIZE, j * SQSIZE)
            j = j + 1
        i = i + 1

    if tila["result"] == 0:
        i,j = 0,0
        while i < len(tila["kentta"][0]):
            j = 0
            while j < len(tila["kentta"]):
                if tila["kentta"][j][i] == "x":
                    haravasto.lisaa_piirrettava_ruutu("x", i * SQSIZE, j * SQSIZE)
                j = j + 1
            i = i + 1

    if tila["result"] == 1:
        i,j = 0,0
        while i < len(tila["kentta"][0]):
            j = 0
            while j < len(tila["kentta"]):
                if tila["kentta"][j][i] == "x":
                    haravasto.lisaa_piirrettava_ruutu("f", i * SQSIZE, j * SQSIZE)
                j = j + 1
            i = i + 1
    haravasto.piirra_ruudut()
    

def main(width, height, mineQnt):
    clearTable()
    haravasto.lataa_kuvat("./spritet")
    kentta = []
    for rivi in range(height):
        kentta.append([])
        for sarake in range(width): 
            kentta[-1].append(" ")
    tila["kentta"] = kentta
    
    jaljella = []
    for x in range(height):
        for y in range(width):
            jaljella.append((x, y))

    mineService.miinoita(tila["kentta"], jaljella, mineQnt) 
    haravasto.luo_ikkuna(width * SQSIZE, height * SQSIZE)
    haravasto.piirra_tausta()
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    game()
    return(tila["time"] - 3, tila["result"], tila["moves"])

def clearTable():
    tila["kentta"] = None
    tila["time"] = 0
    tila["end"] = 0
    tila["result"] = 3
    tila["available"] = 9
    tila["timeOut"] = 0
    tila["moves"] = 0


