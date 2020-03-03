
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
        numberOfKeyWords = int(input("Amount of keys = "))
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
    numberOfRounds = 22
elif wordSize == 24 and numberOfKeyWords == 3:
    numberOfRounds = 22
elif wordSize == 24 and numberOfKeyWords == 4:
    numberOfRounds = 23
elif wordSize == 32 and numberOfKeyWords == 3:
    numberOfRounds = 26
elif wordSize == 32 and numberOfKeyWords == 4:
    numberOfRounds = 27
elif wordSize == 48 and numberOfKeyWords == 1:
    numberOfRounds = 28
elif wordSize == 48 and numberOfKeyWords == 3:
    numberOfRounds = 29
elif wordSize == 64 and numberOfKeyWords == 2:
    numberOfRounds = 32
elif wordSize == 64 and numberOfKeyWords == 3:
    numberOfRounds = 33
elif wordSize == 64 and numberOfKeyWords == 4:
    numberOfRounds = 34

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


def leftRotate(num, amount):
    value = (num << amount) | (num >> (wordSize - amount))
    valueMod = value % (2 ** wordSize)
    return valueMod


def rightRotate(num, amount):
    value = (num >> amount) | (num << (wordSize - amount))
    valueMod = value % (2 ** wordSize)
    return valueMod


for i in range(numberOfRounds - 2):  # source: https://eprint.iacr.org/2013/404.pdf page 20
    Key2shiftRight = rightRotate(keyList2[i], shiftRightAmount)
    Key2plusKey1 = (Key2shiftRight + keyList1[i]) % (2 ** wordSize)
    Key2Final = Key2plusKey1 ^ i
    keyList2.append(Key2Final)
    Key1shiftLeft = leftRotate(keyList1[i], shiftLeftAmount)
    Key1Final = Key1shiftLeft ^ Key2Final
    keyList1.append(Key1Final)

for i in range(numberOfRounds - 1):  # source: https://eprint.iacr.org/2013/404.pdf page 20
    encryptWord1ShiftRight = rightRotate(encryptWord1, shiftRightAmount)
    encryptWord1plusEncryptWord2 = (encryptWord1ShiftRight + encryptWord2) % (2 ** wordSize)
    encryptWord1 = encryptWord1plusEncryptWord2 ^ keyList1[i]
    encryptWord2ShiftLeft = leftRotate(encryptWord2, shiftLeftAmount)
    encryptWord2 = encryptWord2ShiftLeft ^ encryptWord1

print("The word " + str(hex(unencryptedWord1)) + " got encrypted to " + str(hex(encryptWord1)) + " and the word " + str(
    hex(unencryptedWord2)) + " got encrypted to " + str(hex(encryptWord2)))
