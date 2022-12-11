def ProcessCpuInstructions(input):
    countPoints = [20, 60, 100, 140, 180, 220]
    signalStrength = 0
    valueToAddNextCycle = 0
    xValue = 1
    cycleCount = 1
    lineIndex = 0
    skipCycle = False

    while cycleCount <= 220:
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
    return signalStrength


def main():
    with open("input.txt", "r") as file:
        data = file.readlines()

    signalStrength = ProcessCpuInstructions(data)
    print("Signal Strength: %s" % signalStrength)


main()
