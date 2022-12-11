def ProcessCpuInstructions(input):
    countPoints = [20, 60, 100, 140, 180, 220]
    xValueArray = []
    signalStrength = 0
    valueToAddNextCycle = 0
    xValue = 1
    cycleCount = 1
    lineIndex = 0
    skipCycle = False

    while lineIndex <= 240 and lineIndex < 144:
        if skipCycle == True:
            skipCycle = False
        else:
            xValue += valueToAddNextCycle
            valueToAddNextCycle = 0
            splitLine = input[lineIndex].replace("\n", "").split(" ")
            if splitLine[0] == "addx":
                skipCycle = True
                valueToAddNextCycle = int(splitLine[1])
                print("Count:", cycleCount, splitLine[1], valueToAddNextCycle)
            lineIndex += 1

        if cycleCount in countPoints:
            signalStrength += cycleCount * xValue
            print(
                "Count", cycleCount, "Value", xValue, "Signal Strength", signalStrength
            )
        cycleCount += 1
        xValueArray.append(xValue)
    return signalStrength, xValueArray


def CalculateRenderedImage(xValueArray):
    output = ""
    for y in range(0, 6):
        row = ""
        for x in range(0, 40):
            idx = y * 40 + x
            print("Index: ", idx)
            if (
                xValueArray[idx] == x
                or xValueArray[idx] == max(x - 1, 0)
                or xValueArray[idx] == min(x + 1, 39)
            ):
                row = row + "#"
            else:
                row = row + "."
        output = output + row + "\n"
    return output


def main():
    with open("input.txt", "r") as file:
        data = file.readlines()

    signalStrength, xValueArray = ProcessCpuInstructions(data)
    print("Signal Strength: %s" % signalStrength)
    print(len(xValueArray))

    renderArray = CalculateRenderedImage(xValueArray)

    print(renderArray)


main()
