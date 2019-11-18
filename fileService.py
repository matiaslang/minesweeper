import datetime
FILE = "mineSweeperRecords.txt"

"""
file to handle all the communications with the file.
The file is used to save records to, and named mineSweeperRecords.txt and located in
same directory with the program
"""

def writeRecords(duration, size_x, size_y, result, moves):
    """
    function to write records to existing file with name "mineSweeperRecords.txt".
    If no file exist, the program will create one for you.

    Opens the file, writes the row, and closes the file.

    @params duration: duration of the played game in seconds
    @params size_x: width of the board in squares(normally 40*40 pixels)
    @params size_y: height of the board in squares(normally 40*40 pixels)
    @params result: the result of the game. 1 = win, 0 = lose.
    @params moves: the amount of moves / clicks the user made during the game
    @returns: None
    """
    if duration < 60:
        duration = round(duration, 1)
        duration = str(duration) + ' seconds'
    elif duration > 60:
        duration = duration / 60
        duration = round(duration, 1)
        duration = str(duration) + ' minutes'
    file = open(FILE, "a+")
    if result == 1:
        text = 'result = WON - Boardsize: {} by {} - game lasted {} - played on {} - moves {}\n'.format(size_x, size_y, duration, datetime.date.today(), moves)
    elif result == 0:
        text = 'result = LOST - Boardsize: {} by {} - game lasted {} - played on {} - moves {}\n'.format(size_x, size_y, duration, datetime.date.today(), moves)
    file.write(text)
    file.close()

def readRecords():
    """
    Reads all written records of the game. 
    """
    file = open(FILE, "r")
    for i in file:
        print(i)