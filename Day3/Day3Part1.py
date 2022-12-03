class Backpack:

    def __init__(self, input):
        inputClean = input.strip()
        compartmentAList = []
        compartmentBList = []
        # print("Clean Input = %s" %inputClean)
        for count, value in enumerate(inputClean):

            if count < len(inputClean)/2:
                compartmentAList += value
            else:
                compartmentBList += value
        
        self.compartmentA = compartmentAList
        self.compartmentB = compartmentBList

        self.determineCommonLetter()
        self.determineLetterPoints()



    def determineCommonLetter(self):
        for letter in self.compartmentA:
            for otherLetter in self.compartmentB:
                if letter == otherLetter:
                    self.commonLetter = letter

    def determineLetterPoints(self):
        asciiValue = ord(self.commonLetter)
        if self.commonLetter.isupper():
            self.pointValue = asciiValue - 38
        else:
            self.pointValue = asciiValue - 96


def determineTotalPriorityValues(input):
    totalPoints = 0
    for value in input:
        backpack = Backpack(value)

        totalPoints += backpack.pointValue
    
    return totalPoints



def main():
    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()
    
    print(determineTotalPriorityValues(fileOutput))

main()



    
