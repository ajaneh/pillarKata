from globalValues import *
#pencilCurrentUse : ['write', 'sharpen', 'erase']
def PencilWrite(textToWrite, pencilDurability, pencilLength, pencilCurrentUse, currentPaper = ""):
    global durability
    global paper
    paper = currentPaper
    #init just return text
    if pencilCurrentUse == 'write':
        if currentPaper == "":
            durability = pencilDurability
        for letter in textToWrite:
            paper += CanLetterBeWritten(letter)
    if pencilCurrentUse == 'sharpen':
        durability = pencilDurability
    return currentPaper + paper

#When a pencil is sharpened, it regains its initial point durability


def CanLetterBeWritten(letter):
    global durability
    if letter in ["", " ", "\n"]:
        return letter
    if letter.islower():
        cost = 1
    if letter.isupper():
        cost = 2
    if cost <= durability:
        durability -= cost
        return letter
    else:
        return " "

