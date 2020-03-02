import numpy

print("Choose a word size of: 16, 24, 32, 48 of 64")
listWordSize = [16, 24, 32, 48, 64]
wordSizeLoop = True
wordSize = 0
numberOfKeyWords = 0
numberOfRounds = 0
shiftLeftAmount = 0
shiftRightAmount = 0
while wordSizeLoop:
    try:
        wordSize = int(input("Word size = "))
        if wordSize not in listWordSize:
            raise ValueError
        wordSizeLoop = False
    except ValueError:
        print("This number is not one of the options")

if wordSize == 16:
    KeyWordsLoop = False
    numberOfKeyWords = 4
    shiftLeftAmount = 2
    shiftRightAmount = 7
else:
    KeyWordsLoop = True
    shiftLeftAmount = 3
    shiftRightAmount = 8
    print("Choose the number of key words based on the word size.")
    print("if the word size is 24 or 32, then the amount of keys is either 3 or 4.")
    print("if the word size is 48, then the amount of keys is either 2 or 3.")
    print("if the word size is 64, then the amount of keys is either 2, 3 or 4.")

listKeyWords = [2, 3, 4]
while KeyWordsLoop:
    try:
        numberOfKeyWords = int(input("Word size = "))
        if numberOfKeyWords not in listKeyWords:
            raise ValueError
        elif (wordSize == 24 or wordSize == 32) and numberOfKeyWords == 2:
            raise ValueError
        elif wordSize == 48 and numberOfKeyWords == 4:
            raise ValueError
        KeyWordsLoop = False
    except ValueError:
        print("This is not a correct number")

if wordSize == 16:
    numberOfRoundsLoop = False
    numberOfRounds = 22
else:
    numberOfRoundsLoop = True
    print("Choose the number of rounds based on the word size.")
    print("if the word size is 24, then the amount of rounds is either 22 or 23.")
    print("if the word size is 32, then the amount of rounds is either 26 or 27.")
    print("if the word size is 48, then the amount of rounds is either 28 or 29.")
    print("if the word size is 64, then the amount of rounds is either 32, 33 or 34.")

listRounds = [22, 23, 26, 27, 28, 29, 32, 33, 34]
while numberOfRoundsLoop:
    try:
        numberOfRounds = int(input("Number of rounds = "))
        if numberOfRounds not in listRounds:
            raise ValueError
        elif wordSize == 24 and not (numberOfRounds == 22 or numberOfRounds == 23):
            raise ValueError
        elif wordSize == 32 and not (numberOfRounds == 26 or numberOfRounds == 27):
            raise ValueError
        elif wordSize == 48 and not (numberOfRounds == 28 or numberOfRounds == 29):
            raise ValueError
        elif wordSize == 64 and not (numberOfRounds == 32 or numberOfRounds == 33 or numberOfRounds == 34):
            raise ValueError
        numberOfRoundsLoop = False
    except ValueError:
        print("This is not a correct number")

print("the word size is " + str(wordSize) + ", the amount of keys is " + str(numberOfKeyWords) + " and the number of rounds is " + str(numberOfRounds))

encryptWord1 = 0
unencryptedWord1 = 0
encryptWord2 = 0
unencryptedWord2 = 0
input1Loop = True
while input1Loop:
    try:
        input1 = input("Enter your first hexadecimal number to be encrypted = ")
        encryptWord1 = int(input1, 16)
        unencryptedWord1 = encryptWord1
        input1Loop = False
    except ValueError:
        print("This is not a hexadecimal number")

input2Loop = True
while input2Loop:
    try:
        input2 = input("Enter your second hexadecimal number to be encrypted = ")
        encryptWord2 = int(input2, 16)
        unencryptedWord2 = encryptWord2
        input2Loop = False
    except ValueError:
        print("This is not a hexadecimal number")

keyList1 = []
keyList2 = []
for i in range(numberOfKeyWords):  # for lus van 0 tot numberOfKeyWords-1
    KeyLoop = True
    while KeyLoop:
        try:
            inputKey = input("Enter a hexadecimal number as your key = ")
            hexadecimalKey = int(inputKey, 16)
            KeyLoop = False
            if i == 0:
                keyList1.append(hexadecimalKey)
            else:
                keyList2.append(hexadecimalKey)
        except ValueError:
            print("This is not a hexadecimal number")

for i in range(numberOfRounds-2):  # source: https://eprint.iacr.org/2013/404.pdf page 20
    Key2shiftRight = numpy.right_shift(keyList2[i], shiftRightAmount)
    Key2plusKey1 = (Key2shiftRight + keyList1[i]) % wordSize
    Key2Final = Key2plusKey1 ^ i
    keyList2.append(Key2Final)
    Key1shiftLeft = numpy.left_shift(keyList1[i], shiftLeftAmount)
    Key1Final = Key1shiftLeft ^ Key2Final
    keyList1.append(Key1Final)

for i in range(numberOfRounds-1):  # source: https://eprint.iacr.org/2013/404.pdf page 20
    encryptWord1ShiftRight = numpy.right_shift(encryptWord1, shiftRightAmount)
    encryptWord1plusEncryptWord2 = (encryptWord1ShiftRight + encryptWord2) % wordSize
    encryptWord1 = encryptWord1plusEncryptWord2 ^ keyList1[i]
    encryptWord2ShiftLeft = numpy.left_shift(encryptWord2, shiftLeftAmount)
    encryptWord2 = encryptWord2ShiftLeft ^ encryptWord1


print("The word " + str(hex(unencryptedWord1)) + " got encrypted to " + str(hex(encryptWord1)) + " and the word " + str(hex(unencryptedWord2)) + " got encrypted to " + str(hex(encryptWord2)))
