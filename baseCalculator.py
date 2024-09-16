import sys
"""

@author
"""
# Base 8 and Base 16
octal = ['0', '1', '2', '3', '4', '5', '6', '7']
hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def decimalToBinary(decimalNum):
    binaryNum = ""

    for i in range (8):
        if(decimalNum % 2 == 0):
            binaryNum = "0" + binaryNum
        else:
            binaryNum = "1" + binaryNum
        decimalNum //= 2

    return binaryNum

def negativeDecimalToBinary(decimalNum):
    finalNum = ""
    if(decimalNum <= 0 and decimalNum >= -127):
        binaryNum = decimalToBinary(decimalNum * -1)
        reversedBinaryNum = ""
        for char in binaryNum:
            if(char == "1"):
                reversedBinaryNum += "0"
            else:
                reversedBinaryNum += "1"
        
        if(reversedBinaryNum[7] == "0"):
            finalNum = reversedBinaryNum[:7] + "1"
        else:
            for i in range (len(reversedBinaryNum) - 2, -1, -1):
                if(reversedBinaryNum[i] == "0"):
                    finalNum = reversedBinaryNum[:i] + "1" + finalNum + "0"
                    break
                else:
                    finalNum += "0"
    else:
        finalNum = "10000000"

    
    return finalNum
    
def binaryToDecimal(binaryNum):
    decimalNum = 0
    base = 1
    if(len(binaryNum) == 8):
        for i in range (len(binaryNum) - 1, 0, -1):
            # if(not binaryNum[i] == "0" or not binaryNum[i] == "1"):
            #     print("Please enter a binary number.")
            if(binaryNum[i] == "1"):
                decimalNum += base
            base *= 2
    return decimalNum

def negativeBinaryToDecimal(binaryNum):
    finalNum = ""
    reversedBinaryNum = ""
    
    if(binaryNum[7] == "1"):
        reversedBinaryNum = binaryNum[:7] + "0"
    else:
        for i in range (len(binaryNum) - 2, -1, -1):
            if(binaryNum[i] == "1"):
                reversedBinaryNum = binaryNum[:i] + "0" + reversedBinaryNum + "1"
                break
            else:
                reversedBinaryNum += "1"
    
    for char in reversedBinaryNum:
            if(char == "1"):
                finalNum += "0"
            else:
                finalNum += "1"
    
    return(binaryToDecimal(finalNum))

# Start of the main() code
while(True):
    print(
        "\t\tWhat would you like to convert?\n\n\t\tBinary\t\tDecimal")
    print("\t\tTo\t\tTo\t\tExit")
    print("\t\tDecimal\t\tBinary")
    userInput = input("\t\t1\t\t2\t\t3\n\t\t")

    if(userInput[0:3].lower() == "dec" or userInput == "2"):
        while True:
            try:
                decimal = int(input("Please enter a decimal number between -128 and 127: "))
                break
            except ValueError:
                print("Please enter a valid number.\n")

        binary = ""
        complement = ""
        if(decimal >= 0 and decimal <= 127):
            binary = decimalToBinary(decimal)
            complement = negativeDecimalToBinary(decimal * -1)
        elif(decimal <= 0 and decimal >= -128):
            binary = negativeDecimalToBinary(decimal)
            complement = decimalToBinary(decimal * -1)
        else:
            binary = "The number isn't in the workable range."
            complement = "The number isn't in the workable range.\n"

        print("Decimal: %d \nBinary: %s\nComplement: %s\n" % (decimal, binary, complement))
    elif(userInput[0:3].lower() == "bin" or userInput == "1"):
        eightDigits = False
        decimal = 0
        while(not eightDigits):
            test = input("Please enter a 8-digit binary number: ")
            if(len(test) == 8):
                break
        if(test[0] == "1"):
            decimal = negativeBinaryToDecimal(test) * -1
        else:
            decimal = binaryToDecimal(test)
        print("Decimal: %d\n" % decimal)
    elif(userInput[0].lower() == "e" or userInput == "3"):
        print()
        sys.exit()
    else:
        print("Please retype your response.\n")
