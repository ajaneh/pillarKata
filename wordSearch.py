
class PaperWriter:

    def __init__(self, pencilDurability, pencilLength, eraserDurability, paper = ""):
        self.durability = pencilDurability
        self.paper = paper
        self.pencilLength = pencilLength
        self.eraserDurability = eraserDurability
        self.specificDurability = pencilDurability


    def sharpen(self):
        if self.pencilLength > 0:
            self.durability = self.specificDurability
            self.pencilLength -= 1
        else:
            print "This pencil can't be sharpened anymore"

    def edit(self, textToAdd):
        splitPaper = self.paper.split(" ")
        spaceStart,spaceEnd = -1, 0
        for ind,i in enumerate(splitPaper):
            if not i and spaceStart == -1:
                spaceStart = ind
            if i and spaceStart != -1:
                spaceEnd = ind
                break

        splitPaper[spaceStart] = " ".join(splitPaper[spaceStart:spaceEnd])
        splitPaper = [x for x in splitPaper if x != '']
        erasedStringLength = spaceEnd-spaceStart-1
        newWordLength = len(textToAdd)
        if erasedStringLength >= newWordLength:
            for index,word in enumerate(splitPaper):
                if len(word) == erasedStringLength:
                        splitPaper[index] = textToAdd
                        self.paper = " ".join(splitPaper)
                        break
        else:
            newstring = ''
            lengthCountdown = 0
            for index,character in enumerate(self.paper):
                 if index < spaceStart:
                    newstring += character
                 if spaceStart <= index <= spaceEnd -1:
                    newstring += textToAdd[lengthCountdown]
                    lengthCountdown += 1
                 if index > spaceEnd -1:
                     if lengthCountdown != newWordLength:
                         if character != ' ':
                             newstring += '@'
                         else:
                            newstring += textToAdd[lengthCountdown]
                         lengthCountdown += 1
                     else:
                         newstring += character
            self.paper = newstring




    def erase(self, textToManipulate):
        splitTextInReverse = self.paper.split()[::-1]
        for index, word in enumerate(splitTextInReverse):
            if word == textToManipulate:
                splitTextToManipulate = list(textToManipulate)
                for ind,letter in enumerate(splitTextToManipulate[::-1]):
                        if self.eraserDurability > 0:
                            splitTextToManipulate[ind] = " "
                            self.eraserDurability -= 1
                splitTextInReverse[index] = ''.join(splitTextToManipulate)
                break
        self.paper = splitTextInReverse[::-1]
        self.paper = " ".join(self.paper)

    def PencilWrite(self, textToManipulate):
            for letter in textToManipulate:
                self.CanLetterBeWritten(letter)


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

if __name__ == '__main__':
    pencilSpecs = input("Please specify the pencil durability, pencil length, and eraser durability, in that order\n example: '500, 10, 5\n")
    print
    pieceOfPaper = PaperWriter(pencilSpecs[0], pencilSpecs[1], pencilSpecs[2])
    print "Please enter desired action, comma, and text"
    print "example: write, Alex is excited about Pillar!"
    while True:
        action = raw_input("Hello Author! How can I help? write, erase, edit, sharpen, or print\n").lower()
        print action
        try:
            action, textToUse = str(action.split(',')[0]), str(action.split(',')[1])
        except:
            pass
        if action not in ['write', 'erase', 'edit', 'print', 'sharpen'] or not action:
            print("I don't know how to do that, maybe a word processor would suit this task better")
            continue
        if action == 'write':
            pieceOfPaper.PencilWrite(textToUse)
        elif action == 'erase':
            pieceOfPaper.erase(textToUse)
        elif action == 'edit':
            pieceOfPaper.edit(textToUse)
        elif action == 'print':
            print pieceOfPaper.paper
        elif action == 'sharpen':
            pieceOfPaper.sharpen()



