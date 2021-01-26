def convert(string, dictionary):
    result = ""
    string = string.replace("{","").replace(",","").replace("}","")
    for i in range(0,len(string),4):
        search = int((string[i]+string[i+1]+string[i+2]+string[i+3]),0)
        for symbol, number in dictionary.items():
            if number == search:
                result = result+symbol
                break
    return result