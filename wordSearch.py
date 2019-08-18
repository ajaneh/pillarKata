from globalValues import *
#pencilCurrentUse : ['write', 'sharpen', 'erase']
def PencilWrite(textToManipulate, pencilDurability, pencilLength, pencilCurrentUse, currentPaper = ""):
    global durability
    global paper

    #init just return text
    if pencilCurrentUse == 'write':
        paper = currentPaper
        if currentPaper == "":
            durability = pencilDurability
        for letter in textToManipulate:
            paper += CanLetterBeWritten(letter)
    if pencilCurrentUse == 'sharpen':
        durability = pencilDurability
    if pencilCurrentUse == 'erase':
        paper = ""
        splitTextInReverse = currentPaper.split()[::-1]
        splitTextInReverse.remove(textToManipulate)
        currentPaper = splitTextInReverse[::-1]
        currentPaper = " ".join(currentPaper)

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

