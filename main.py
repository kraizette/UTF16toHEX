import ConverterToHEX
import ConverterToUTF16
import EncodingTableLatinandCyrillic
import EncodingTableChinese

if __name__ == '__main__':
    print("input string")
    string = input()
    print("RU, EN, FR, DE - 1, CH - 2")
    language = input()
    if language=='1':
        dictionary = EncodingTableLatinandCyrillic.getdictionary()
    if language=='2':
        dictionary = EncodingTableChinese.getdictionary()
    else:
        dictionary = EncodingTableLatinandCyrillic.getdictionary()
    result = ConverterToHEX.convert(string,dictionary)
    print(result)
    result2 = ConverterToUTF16.convert(result,dictionary)
    print(result2)