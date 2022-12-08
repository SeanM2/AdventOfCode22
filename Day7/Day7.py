sumOfNumberBelow100000 = 0
minSpaceRequired = 0
minimumDirectory = 70000000


class file:
    def __init__(self, name, size, parent) -> None:
        self.name = name.strip()
        self.size = size
        self.parent = parent


class folder:
    def __init__(self, name, parent=None) -> None:
        self.name = name.strip()
        self.listOfFiles = []
        self.listOfFolders = []
        self.parent = parent
        self.directorySize = 0

    def AddNewFolder(self, folderName):
        self.listOfFolders.append(folder(folderName, self))

    def AddNewFile(self, fileName, fileSize):
        self.listOfFiles.append(file(fileName, fileSize, self))

    def GetFolderByName(self, folderName):
        for folder in self.listOfFolders:
            if folder.name == folderName:
                return folder
        print("Could not find %s" % folderName)

    def GetFolderSizes(self, minSpace):
        global sumOfNumberBelow100000, minSpaceRequired, minimumDirectory
        # print(self.name)

        self.directorySize = 0

        for file in self.listOfFiles:
            self.directorySize += file.size

        for folder in self.listOfFolders:
            self.directorySize += folder.GetFolderSizes(minSpace)

        if self.directorySize <= 100000:
            sumOfNumberBelow100000 += self.directorySize

        if (
            minSpace
            and self.directorySize >= minSpaceRequired
            and self.directorySize < minimumDirectory
        ):
            minimumDirectory = self.directorySize
        return self.directorySize


def CreateDirectories(input):
    topFolder = folder("/")
    activeDirectory = topFolder
    # print(topFolder)

    for line in input[1:]:
        # print(activeDirectory.name)
        # print(line)
        splitLine = line.split(" ")
        if "$" in splitLine[0]:
            if "cd" in splitLine[1]:
                if ".." in splitLine[2]:
                    activeDirectory = activeDirectory.parent
                else:
                    activeDirectory = activeDirectory.GetFolderByName(
                        splitLine[2].strip()
                    )
        else:
            if "dir" in splitLine[0]:
                activeDirectory.AddNewFolder(splitLine[1].strip())
            else:
                activeDirectory.AddNewFile(splitLine[1].strip(), int(splitLine[0]))
        # print(activeDirectory.name)
    return topFolder


def main():
    global minSpaceRequired, minimumDirectory
    with open("input.txt", "r") as file:
        fileOutput = file.readlines()

    topFolder = CreateDirectories(fileOutput)
    topFolder.GetFolderSizes(False)
    print("Sum of Directories Below 100,000: %s" % sumOfNumberBelow100000)

    spaceAvailable = 70000000 - topFolder.directorySize
    minSpaceRequired = 30000000 - spaceAvailable
    topFolder.GetFolderSizes(True)

    print("Current Space Available: %s" % spaceAvailable)
    print("Space Required to Delete: %s" % minSpaceRequired)
    print("Smallest Directory to delete: %s" % minimumDirectory)


main()
