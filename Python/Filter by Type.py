
def testInt(myInt):
    if myInt >= 100:
        print("That's a big number!")
    elif myInt < 100:
        print("That's a small number")
    pass

#String

def checkStr(myStr):
    if len(myStr) >= 50:
        print("Long sentence")
    elif len(myStr) < 50:
        print("Short sentence.")
    pass

#List

def checkLs(myList):
    if len(myList) >= 10:
        print("Big list!")
    elif len(myList) < 10:
        print("Short list.")
    pass


checkLs([4,34,22,68,9,13,3,5,7,9,2,12,45,923])