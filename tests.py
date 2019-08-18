from pytest import *
from wordSearch import *


def test_AcceptAStringAndWriteIt(string):
    #don't worry about file in/out yet
    Papers = PaperWriter(100, 1, 1)
    Papers.PencilWrite(string)
    assert Papers.paper == string

def TestDurabilityOnlyWritesLettersWhenSharp(expectedString, string, givenDurability):
    Papers = PaperWriter(givenDurability, 1, 1)
    Papers.PencilWrite(string)
    assert Papers.paper == expectedString

def TestDurabilityResetsWhenSharpened(expectedDurability):
    Papers = PaperWriter(4, 1, 1)
    Papers.PencilWrite("test")
    assert Papers.durability == 0
    Papers.sharpen()
    assert Papers.durability == expectedDurability

def TestEraseFunctionality(initialString, expectedString):
    Papers = PaperWriter(100, 1, 4)
    Papers.PencilWrite("a test is a test when tested")
    Papers.erase("test")
    assert initialString != Papers.paper
    assert expectedString == Papers.paper

def TestEraserDegrades():
    Papers = PaperWriter(100, 1, 5)
    Papers.PencilWrite("test my test")
    Papers.erase("test")
    assert Papers.eraserDurability == 1
    Papers.erase("my")
    assert Papers.eraserDurability == 0

def TestEditingWorksInSimpleNonShiftedScenario():
    Papers = PaperWriter(100, 1, 100)
    Papers.PencilWrite("sally sold seashells on the seashore")
    Papers.erase("sally")
    Papers.edit("alex")
    assert Papers.paper == "alex sold seashells on the seashore"

def TestEditingWorksWhenWordExceedsSpace():
    Papers = PaperWriter(100, 1, 100)
    Papers.PencilWrite("sally did shuffle seashells on the seashore")
    Papers.erase("sally")
    Papers.edit("alexanndra")
    assert Papers.paper == "alexan@@@ashuffle seashells on the seashore"

test_AcceptAStringAndWriteIt("Testing testing")
TestDurabilityOnlyWritesLettersWhenSharp("test", "test", 4)
TestDurabilityOnlyWritesLettersWhenSharp("Tes ", "Test", 4)
TestDurabilityOnlyWritesLettersWhenSharp("Test ", "Tests", 5)
TestDurabilityResetsWhenSharpened(4)
TestEraseFunctionality("a test is a test when tested", "a test is a      when tested")
TestEraserDegrades()
TestEditingWorksInSimpleNonShiftedScenario()
TestEditingWorksWhenWordExceedsSpace()