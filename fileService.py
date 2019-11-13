import datetime
FILE = "mineSweeperRecords.txt"

def writeRecords(duration, size_x, size_y, result, moves):
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
    file = open(FILE, "r")
    for i in file:
        print(i)