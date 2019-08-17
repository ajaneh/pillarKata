from pytest import *
from wordSearch import *
def AcceptAStringAndWriteIt(string, result):
    #don't worry about file in/out yet
    assert string == result

def TestDurabillityOnlyWritesLettersWhenSharp(string, result):
    assert string == result


#AcceptAStringAndWriteIt("Testing testing", PencilWrite("Testing testing"))
TestDurabillityOnlyWritesLettersWhenSharp("test", PencilWrite("test", 4))
TestDurabillityOnlyWritesLettersWhenSharp("Tes ", PencilWrite("Test", 4))
TestDurabillityOnlyWritesLettersWhenSharp("Test ", PencilWrite("Tests", 5))