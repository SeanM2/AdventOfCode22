def determineMove(input):
    if input == "A":
        return "Rock"
    elif input == "B":
        return "Paper"
    elif input == "C":
        return "Scissors"
    else:
        print("Error value on input: " + input)

def determineDesiredResult(input):
    if input == "X":
        return "loss"
    elif input == "Y":
        return "draw"
    elif input == "Z":
        return "win"
    else:
        print("Error value on input: " + input)

def determinePlayerMove(opponentMove, desiredResult):
    if opponentMove not in ("Rock", "Paper", "Scissors") or desiredResult not in ("loss", "draw", "win"):
        print("Invalid inputs in either, Opponent Move: " + opponentMove + ", or Desired Result: " + desiredResult)

    if opponentMove == "Rock":
        if desiredResult == 'win':
            return "Paper"
        elif desiredResult == 'draw':        
            return "Rock"
        else:
            return "Scissors"
    elif opponentMove == 'Paper':
        if desiredResult == 'win':
            return "Scissors"
        elif desiredResult == 'draw':        
            return "Paper"
        else:
            return "Rock"
    else:
        if desiredResult == 'win':
            return "Rock"
        elif desiredResult == 'draw':        
            return "Scissors"
        else:
            return "Paper"


def determinePoints(yourMove, result):
    points = 0

    if yourMove == "Rock":
        points += 1
    elif yourMove == "Paper":
        points += 2
    else:
        points += 3
    
    if result == 'win':
        points += 6
    elif result == "draw":
        points += 3
    
    return points
    
def determineTotalPoints(inputArray):
    totalPoints = 0

    for line in inputArray:
        #print(line)
        split = line.replace("\n","").split(" ")
        #print(split)
        opponentMove = determineMove(split[0])

        desiredResult = determineDesiredResult(split[1])


        yourMove = determinePlayerMove(opponentMove, desiredResult)

        points = determinePoints(yourMove, desiredResult)

        # print("Input: " + line + ", Desired Result: " + desiredResult + ", Your Move: " + yourMove + ", Points: " + str(points))

        totalPoints += points

    return totalPoints

def main():

    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()

    print("Total Points = " + str(determineTotalPoints(fileOutput)))
