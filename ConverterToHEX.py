from EncodingTable import dictionary

def getitem(symbol):
    result = f'{symbol}'
    return dictionary[result]

def convert(string):
    result = '{'
    for i in string:
        result = result + f"'{getitem(i)}',"
    result = result[:-1] + '}'
    return result
