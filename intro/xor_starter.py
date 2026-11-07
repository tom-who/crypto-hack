# I sort of messed with this in later challenges so its slightly broken. But it's here anyway

import time

def convert(string):
    binary_array = []
    for i in range(len(string)):
        num = string[i]
        array = []
        while num >= 0:
            if num % 2 == 0:
                array.append(0)
            elif (num % 2) != 0:
                array.append(1)
            if num == 0:
                break
            num = num // 2
        binary_array.append(array[::-1])
    return binary_array

binaryWord = convert(b'label')
binaryNum = convert([13])[0]
#print(convert([97]))
#print(binaryWord)

# Ik its terrible but just added padding to make sure the things are the same size.

binaryNum = binaryNum[::-1]

for i in range(3):
    binaryNum.append(0)
binaryNum = binaryNum[::-1]
#print(binaryNum)
#print(len(binaryNum))
#print(len(binaryWord[0]))

def xor(binaryWord, binaryNum):
    finalXor = []
    for i in range(len(binaryWord)):
        #print(f"[*] XORing {binaryWord[i]} with {binaryNum}")
        for j in range(len(binaryNum)):
            #print(f"{binaryNum[j]} | {binaryWord[i][j]} : ", end="")
            if binaryWord[i][j] == binaryNum[j]:
                binaryWord[i][j] = 0
                #print(0)
            elif binaryWord[i][j] != binaryNum[j]:
                binaryWord[i][j] = 1
                #print(1)
        #print(binaryWord[i])
        finalXor.append(binaryWord[i])
    return finalXor

finalXor = xor(binaryWord, binaryNum)
#print("\n\n")
#print(finalXor)
#print("\n\n")
finalXor = [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1]
def reverse(finalXor):
    power = 208
    charPlaceholder = 0
    for i in range(len(finalXor)):
        if finalXor[i] == 1:
            charPlaceholder = charPlaceholder + pow(2, (power - i))
    return charPlaceholder

#print("\n")
finalXor = reverse(finalXor)
print(finalXor)
