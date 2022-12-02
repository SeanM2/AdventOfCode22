
class elfObject:
    

    def __init__(self, calories):
        self.calorieEntry = []
        self.calorieEntry.append(calories)
    
    def addNewEntry(self, entry):
        self.calorieEntry.append(entry)
    
    def calculateTotalCalories(self):
        total = 0
        for entry in self.calorieEntry:
            total += entry
        self.totalCalories = total
        return total




fileOutput = []
with open('input.txt', 'r') as file:
    fileOutput = file.readlines()

newElf = True
elfArray = []
for count, line in enumerate(fileOutput):
    if line =="\n":
        print("New Elf")
        newElf = True
    else:
        if newElf:
            elfArray.append(elfObject(int(line)))
            newElf= False
        else:
            elfArray[len(elfArray)-1].addNewEntry(int(line))


maxCalories = 0

for elf in elfArray:
    elfCalories = elf.calculateTotalCalories()
    if elfCalories > maxCalories:
        maxCalories = elfCalories

sortedElf = sorted(elfArray, key=lambda elf: elf.totalCalories, reverse=True)

print(sortedElf[0].totalCalories + sortedElf[1].totalCalories + sortedElf[2].totalCalories)
            

    




