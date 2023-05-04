import os
from colorama import Fore, Back
from random import randint

def printWhite(data):
    print(Fore.WHITE, data, end="", sep="")

def printRed(data):
    print(Fore.RED, data, end="", sep="")


def printGreen(data):
    print(Fore.GREEN, data, end="", sep="")


def screenXO(screen):
    os.system('cls')

    corners = {
        "upperLeft": "┌",  
        "upperRight": "┐",  
        "mediumLeft": "├",  
        "mediumRight": "┤",  
        "bottomLeft": "└",  
        "bottomRight": "┘",  
        "upperMid": "┬",  
        "mediumMid": "┼",  
        "bottomMid": "┴"  
    }
    lines = {
        "vertical": "│",  
        "horizontal": "─"  
    }

    size = len(screen)

    verticalLine = [lines["horizontal"] * 3] * 3

    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["mediumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)

    printWhite(corners["upperLeft"] + verticalUp + corners["upperRight"] + "\n")

    for i, row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if j > 0:
                printGreen(" X ")
            elif j < 0:
                printRed(" O ")
            else:
                printWhite("   ")
            printWhite(lines["vertical"])
        print()
        if i < size - 1:
            printWhite(corners["mediumLeft"] + verticalMid + corners["mediumRight"] + "\n")

    printWhite(corners["bottomLeft"] + verticalDown + corners["bottomRight"] + "\n")


rozmiar = 3
dane = []
for i in range(rozmiar):
    kolumna = [0 for i in range(rozmiar)]
    dane.append(kolumna)

screenXO(dane)

tura = 1
while True:
    screenXO(dane)
    #print(dane)
    if tura == 1:
        printGreen("Twoj ruch\n")
        x = int(input("Podaj wsp x: "))
        y = int(input("Podaj wsp y: "))
        if dane[x][y] != 0:
            print("Nie możesz zająć pola przeciwnikowi\n")
        else:
            dane[x][y] = tura
            tura *= -1
    else:
       x = randint(0,2)
       y = randint(0,2)
       if dane[x][y] != 0:
          print() 
       else:
            dane[x][y] = tura
            tura *= -1
