
durability = 0
#pencilCurrentUse : ['write', 'sharpen', 'erase']
def PencilWrite(textToWrite, pencilDurability, pencilLength, pencilCurrentUse):
    global durability
    durability = pencilDurability
    paper = ""
    #init just return text
    if pencilCurrentUse == 'write':
        for letter in textToWrite:
            paper += CanLetterBeWritten(letter)
    return paper

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

