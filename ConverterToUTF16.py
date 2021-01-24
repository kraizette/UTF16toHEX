from EncodingTable import invertdictionary

def getitem(symbol):
    return invertdictionary[symbol]

def convert(string):
    result = ""
    string = string.replace("{'","").replace("','","").replace("'}","")
    for i in string:
        result = result+str(getitem(int(i)))
    result = result.replace("['","").replace("],[","").replace("']","")
    return result