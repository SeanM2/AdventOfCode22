def CheckIfAnyValuesAreEqualPart1(v1, v2, v3, v4):
    if v1 in [v2, v3, v4]:
        return True
    elif v2 in [v1, v3, v4]:
        return True
    elif v3 in [v1, v2, v4]:
        return True
    elif v4 in [v1, v2, v3]:
        return True
    else:
        return False

def CheckIfAnyValuesAreEqualPart2(valuesToCheck):
    for i in range(0,len(valuesToCheck)):
        # print("Index: %s" % i)
        # print("Length of Array: %s" % len(valuesToCheck))
        arrayToCheck = valuesToCheck[:]
        value = arrayToCheck[i]
        arrayToCheck.pop(i)
        if value in arrayToCheck:
            return True
    return False

def DetermineMarkerPositionPart1(input):

    inputList = list(input.strip())

    for i in range(3, len(inputList)):
        if CheckIfAnyValuesAreEqualPart1(inputList[i], inputList[i-1], inputList[i-2], inputList[i-3]) is False:
            return i+1

def DetermineMarkerPositionPart2(input):

    inputList = list(input.strip())

    for i in range(13, len(inputList)):
        if CheckIfAnyValuesAreEqualPart2(inputList[i-13:i+1]) is False:
            return i+1



def main():
    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()

    print(DetermineMarkerPositionPart2(fileOutput[0]))

main()
    