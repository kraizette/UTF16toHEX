import ConverterToHEX
import ConverterToUTF16

if __name__ == '__main__':
    print("input string")
    string = input()
    result = ConverterToHEX.convert(string)
    print(result)
    result2 = ConverterToUTF16.convert(result)
    print(result2)