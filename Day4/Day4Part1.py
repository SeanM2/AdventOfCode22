

def determineNumberOfContained(input):
    numberWithClash = 0
    for row in input:
        splitInput = row.split(",")
        shiftA = splitInput[0].split("-")
        shiftB = splitInput[1].split("-")

        if int(shiftA[0]) >= int(shiftB[0]) and int(shiftA[1]) <= int(shiftB[1]):
            numberWithClash += 1
        elif int(shiftB[0]) >= int(shiftA[0]) and int(shiftB[1]) <= int(shiftA[1]):
            numberWithClash += 1

    return numberWithClash
def main():
    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()
    
    print(determineNumberOfContained(fileOutput))

main()
    