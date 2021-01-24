dictionary = {'A': 0,
              'B': 1,
              'C': 2,
              'D': 3
              }

def getUTF16table():
    return dictionary

def getHEXtable():
    newdictionary ={}
    for k,v in dictionary.items():
        newdictionary.setdefault(v,[]).append(k)
    return newdictionary

invertdictionary = getHEXtable()