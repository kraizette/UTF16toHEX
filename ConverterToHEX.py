def getitem(symbol, dictionary):
    result = f'{symbol}'
    return dictionary[result]

def convert(string, dictionary):
    result = '{'
    for i in string:
        num = getitem(i, dictionary)
        symbol = "0x%02X" % num
        result = result + f"{symbol},"
    result = result[:-1] + '}'
    return result
