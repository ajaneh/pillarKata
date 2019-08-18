from pytest import *
from wordSearch import *
from globalValues import *
def AcceptAStringAndWriteIt(string, result):
    #don't worry about file in/out yet
    assert string == result

def TestDurabilityOnlyWritesLettersWhenSharp(string, result):
    assert string == result

#When a pencil is sharpened, it regains its initial point durability
#Need to refactor to accept length and mode
def TestDurabilityResetsWhenSharpened(expectedDurability, useFunction):
    print durability, expectedDurability
    assert durability == expectedDurability



AcceptAStringAndWriteIt("Testing testing", PencilWrite("Testing testing", 100, 1, 'write'))
TestDurabilityOnlyWritesLettersWhenSharp("test", PencilWrite("test", 4, 1, 'write'))
TestDurabilityOnlyWritesLettersWhenSharp("Tes ", PencilWrite("Test", 4,1, 'write'))
TestDurabilityOnlyWritesLettersWhenSharp("Test ", PencilWrite("Tests", 5, 1, 'write'))
TestDurabilityResetsWhenSharpened(0, PencilWrite("test", 4, 1, 'write'))
#globals make testing difficult
#TestDurabilityResetsWhenSharpened(4, PencilWrite("", 4, 1, 'sharpen', 'test'))