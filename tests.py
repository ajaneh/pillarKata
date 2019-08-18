from pytest import *
from wordSearch import *
from globalValues import *
def AcceptAStringAndWriteIt(string, result):
    #don't worry about file in/out yet
    assert string == result

def TestDurabilityOnlyWritesLettersWhenSharp(string, result):
    assert string == result

def TestDurabilityResetsWhenSharpened(expectedDurability, *args):
    PencilWrite(*args)
    assert durability == expectedDurability

def TestEraseFunctionality(initialString, expectedString, resultingString):
    assert initialString != resultingString
    assert expectedString == resultingString

AcceptAStringAndWriteIt("Testing testing", PencilWrite("Testing testing", 100, 1, 'write'))
TestDurabilityOnlyWritesLettersWhenSharp("test", PencilWrite("test", 4, 1, 'write'))
TestDurabilityOnlyWritesLettersWhenSharp("Tes ", PencilWrite("Test", 4,1, 'write'))
TestDurabilityOnlyWritesLettersWhenSharp("Test ", PencilWrite("Tests", 5, 1, 'write'))
TestDurabilityResetsWhenSharpened(0, "test", 4, 1, 'write')
#globals make testing difficult
#TestDurabilityResetsWhenSharpened(4, "", 4, 1, 'sharpen', 'test')
TestEraseFunctionality("a test is a test when tested", "a test is a when tested",
                       PencilWrite("test", 100, 1, 'erase', 'a test is a test when tested'))