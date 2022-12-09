class Tree:
    def __init__(self, height) -> None:
        self.height = height
        self.visible = True


def CreateForest(input):
    forest = []
    for row in input:
        rowArray = list(row.strip())
        treeArray = []
        for tree in rowArray:
            treeArray.append(Tree(int(tree)))
        forest.append(treeArray)
    return forest


def CheckVisibilityToEdge(forest, posX, posY):

    checkVisibilityStatus = [True, True, True, True]

    for i in range(0, posX):
        if forest[i][posY].height >= forest[posX][posY].height:
            checkVisibilityStatus[0] = False
    for i in range(posX + 1, len(forest)):
        if forest[i][posY].height >= forest[posX][posY].height:
            checkVisibilityStatus[1] = False
    for i in range(0, posY):
        if forest[posX][i].height >= forest[posX][posY].height:
            checkVisibilityStatus[2] = False
    for i in range(posY + 1, len(forest[0])):
        if forest[posX][i].height >= forest[posX][posY].height:
            checkVisibilityStatus[3] = False

    if True in checkVisibilityStatus:
        return True
    else:
        return False


def DetermineTreeScenicRating(forest, posX, posY):

    visibleTrees = [0, 0, 0, 0]
    print("X:", posX, "Y:", posY, "Height:", forest[posX][posY].height)

    for i in reversed(range(0, posX)):
        visibleTrees[0] += 1
        print("Up: %s" % forest[i][posY].height)
        if forest[i][posY].height >= forest[posX][posY].height:
            break
    for i in range(posX + 1, len(forest)):
        visibleTrees[1] += 1
        print("Down: %s" % forest[i][posY].height)
        if forest[i][posY].height >= forest[posX][posY].height:
            break
    for i in reversed(range(0, posY)):
        visibleTrees[2] += 1
        print("Left: %s" % forest[posX][i].height)
        if forest[posX][i].height >= forest[posX][posY].height:
            break
    for i in range(posY + 1, len(forest[0])):
        visibleTrees[3] += 1
        print("Right: %s" % forest[posX][i].height)
        if forest[posX][i].height >= forest[posX][posY].height:
            break
    return visibleTrees[0] * visibleTrees[1] * visibleTrees[2] * visibleTrees[3]


def DetermineForestVisibility(forest):
    numberOfHiddenTree = 0
    highestSceneryScore = 0
    for x in range(1, len(forest) - 1):
        for y in range(1, len(forest[0]) - 1):
            scenicRating = DetermineTreeScenicRating(forest, x, y)
            if scenicRating > highestSceneryScore:
                highestSceneryScore = scenicRating
            if CheckVisibilityToEdge(forest, x, y) is False:
                print(
                    "X: " + str(x) + ", Y: " + str(y),
                    ", Not Visible. Tree Height: " + str(forest[x][y].height),
                )
                forest[x][y].visible = False
                numberOfHiddenTree += 1
    return len(forest) * len(forest[0]) - numberOfHiddenTree, highestSceneryScore


def main():
    with open("input.txt", "r") as file:
        data = file.readlines()
    forest = CreateForest(data)
    visibility, sceneryRating = DetermineForestVisibility(forest)
    print("Number of Visible Trees: %s" % visibility)
    print("Highest Scenery Rating: %s" % sceneryRating)


main()
