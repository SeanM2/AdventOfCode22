class GroupSack:

    def __init__(self, input):

        self.backpackAList = input[0].strip()
        self.backpackBList = input[1].strip()
        self.backpackCList = input[2].strip()

        self.determineCommonLetter()
        self.determineLetterPoints()



    def determineCommonLetter(self):
        for letter in self.backpackAList:
            if letter in self.backpackBList and letter in self.backpackCList:
                self.commonLetter = letter

    def determineLetterPoints(self):
        asciiValue = ord(self.commonLetter)
        if self.commonLetter.isupper():
            self.pointValue = asciiValue - 38
        else:
            self.pointValue = asciiValue - 96


def determineTotalPriorityValues(input):
    totalPoints = 0
    for i in range(0, len(input),3):
        groupSack = GroupSack([input[i],input[i+1],input[i+2]])

        totalPoints += groupSack.pointValue
    
    return totalPoints



def main():
    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()
    
    print(determineTotalPriorityValues(fileOutput))

main()



    
