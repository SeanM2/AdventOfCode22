def InsertToEntryArray(entryArray, value, index):
    if value == ' ':
        return entryArray
    else:
        entryArray[index].insert(0,value)
        return entryArray

def CreateArrays(input):
    entryArray = [ [] for i in range(9)]

    for line in (input):
        # print(line)
        lineList = list(line)
        # print(lineList)
        entryArray = InsertToEntryArray(entryArray,lineList[1],0)
        entryArray = InsertToEntryArray(entryArray,lineList[5],1)
        entryArray = InsertToEntryArray(entryArray,lineList[9],2)
        entryArray = InsertToEntryArray(entryArray,lineList[13],3)
        entryArray = InsertToEntryArray(entryArray,lineList[17],4)
        entryArray = InsertToEntryArray(entryArray,lineList[21],5)
        entryArray = InsertToEntryArray(entryArray,lineList[25],6)
        entryArray = InsertToEntryArray(entryArray,lineList[29],7)
        entryArray = InsertToEntryArray(entryArray,lineList[33],8)

    return entryArray

def DetermineInstruction(line):
    """Breaks up the line into moveTarget which is the number of crates to move,\n 
    original index which is the 0 indexed array which the crates should be moved from,\n 
    and then the new index which is the zero indexed target array for the crate(s)"""
    splitLine = line.split(" ")
    moveTarget = int(splitLine[1]) 
    originalIndex = int(splitLine[3]) - 1
    newIndex = int(splitLine[5].strip()) - 1

    return moveTarget, originalIndex, newIndex

def MoveTheCrates9000(entryArray, moveTarget, originalIndex, newIndex):
    while moveTarget > 0:
        valueMoving = entryArray[originalIndex].pop()
        entryArray[newIndex].append(valueMoving)
        moveTarget -= 1
    return entryArray

def MoveTheCrates9001(entryArray, moveTarget, originalIndex, newIndex):
    for i in range(moveTarget):
        valueMoving = entryArray[originalIndex].pop(-moveTarget+i)
        entryArray[newIndex].append(valueMoving)
    return entryArray

def GetFinalAnswer(entryArray):
    output = ''
    for array in entryArray:
        output += array.pop()

    return (output)

def main():
    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()
    
    entryArray = CreateArrays(fileOutput[0:8])
    instructionArray = fileOutput[10:]

    for line in instructionArray:
        moveTarget, originalIndex, newIndex = DetermineInstruction(line)

        entryArray = MoveTheCrates9001(entryArray, moveTarget, originalIndex, newIndex)
    print(GetFinalAnswer(entryArray))
        
main()
