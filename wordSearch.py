
#o simulate, first coarsely and then more faithfully, an ordinary graphite pencil.
#  It includes writing and editing text, point degradation, using the eraser, and sharpening the pencil.
durability = 4
#1) When the pencil is instructed to write a string of text on a sheet of paper,
# the paper should reflect the text that was written.
def PencilWrite(textToWrite):
    paper = ""
    #init just return text
    for letter in textToWrite:
        paper += CanLetterBeWritten(letter)
    return paper

#Lowercase letters should degrade the pencil point by a value of one,
# and capital letters should degrade the point by two.
# Hence when a pencil with a point durability of four
def CanLetterBeWritten(letter):
    global durability
    print durability,letter
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

