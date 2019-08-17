from pytest import *
from wordSearch import *
def AcceptAStringAndWriteIt(string, result):
    #don't worry about file in/out yet
    assert string == result

def TestDurabillityOnlyWritesLettersWhenSharp(string, result):
    print result
    assert string == result


#AcceptAStringAndWriteIt("Testing testing", PencilWrite("Testing testing"))
#TestDurabillityOnlyWritesLettersWhenSharp("test", PencilWrite("test"))
TestDurabillityOnlyWritesLettersWhenSharp("Tes", PencilWrite("Test"))
#TestDurabillityOnlyWritesLettersWhenSharp("Test ", PencilWrite("Tests"))