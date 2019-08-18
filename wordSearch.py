
#pencilCurrentUse : ['write', 'sharpen', 'erase']
specificDurability = 0

class PaperWriter:

    def __init__(self, pencilDurability, pencilLength, eraserDurability, paper = ""):
        self.durability = pencilDurability
        self.paper = paper
        self.eraserDurability = eraserDurability
        self.specificDurability = pencilDurability


    def sharpen(self):
        self.durability = self.specificDurability

    def erase(self, textToManipulate):
        splitTextInReverse = self.paper.split()[::-1]
        splitTextInReverse.remove(textToManipulate)
        self.paper = splitTextInReverse[::-1]
        self.paper = " ".join(self.paper)

    def PencilWrite(self, textToManipulate):
            for letter in textToManipulate:
                self.CanLetterBeWritten(letter)

    #When a pencil is sharpened, it regains its initial point durability


    def CanLetterBeWritten(self,letter):
        cost = 0
        if letter in ["", " ", "\n"]:
            self.paper += letter
            return
        if letter.islower():
            cost = 1
        if letter.isupper():
            cost = 2
        if cost <= self.durability:
            self.durability -= cost
            self.paper += letter
            return
        else:
            self.paper += " "
            return

