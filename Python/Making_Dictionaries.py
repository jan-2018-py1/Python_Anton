#Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. 
#Assume the lists will be of equal length.
#
#Your first function will take in two lists containing some strings.
#
#Hacker Challenge:
#If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

def setdic(list1, list2):
    dict1 = {}
    for i in range(0, len(list1)):
            try:
                dict1[list1[i]] = list2[i]
            except:
                dict1[list1[i]] = ""
    return dict1

def make_dict(list1, list2):
    new_dict = {}

    if len(list1)<len(list2):
        new_dict = setdic(list2, list1)
    elif len(list2)<len(list1):
        new_dict = setdic(list1, list2)
    else:
        new_dict = setdic(list1, list2)

    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print(make_dict(name, favorite_animal))

name = ["Anna", "Eli", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print(make_dict(name, favorite_animal))

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "giraffe", "ticks", "dolphins", "llamas"]

print(make_dict(name, favorite_animal))