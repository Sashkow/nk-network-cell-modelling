def addSucceedingZeroes(maxNumber,number):
    stringNumber = str(number)
    stringNumberLength = len(stringNumber)
    wantedStringNumberLength = len(str(maxNumber))
    stringNumber = '0'*(wantedStringNumberLength-stringNumberLength)+stringNumber
    return stringNumber

def toBinString(maxNumber, number):
    return addSucceedingZeroes(int('1'*maxNumber),(bin(number)[2:]) )

def boolListToInt(boolList):
    s=""
    for item in boolList:
        s+=str(item)
    return int("0b"+s,base=2)


#42-> 32+8+2 -> [1,0,1,0,1,0]
def decimalIntToBinaryList(decimalInt):
    return list(bin(decimalInt)[2:])

def boolListToString(lst):
    reStr=""
    for item in lst:
        reStr+=str(item)
    return reStr
