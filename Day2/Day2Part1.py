def determineMove(input):
    if input == "A" or input == "X":
        return "Rock"
    elif input == "B" or input == "Y":
        return "Paper"
    elif input == "C" or input == "Z":
        return "Scissors"
    else:
        print("Error value on input: " + input)

def determineResult(opponentMove, yourMove):
    if yourMove == opponentMove:
        return 'draw'
    
    if yourMove == "Rock":
        if opponentMove == "Paper":
            return 'loss'
        elif opponentMove == "Scissors":
            return 'win'
    elif yourMove == 'Paper':
        if opponentMove == 'Rock':
            return 'win'
        elif opponentMove == "Scissors":
            return 'loss'
    elif yourMove == 'Scissors':
        if opponentMove == 'Paper':
            return 'win'
        elif opponentMove == 'Rock':
            return 'loss'


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
    # print(line)
        split = line.replace("\n","").split(" ")
        # print(split)
        opponentMove = determineMove(split[0])
        yourMove = determineMove(split[1])

        result = determineResult(opponentMove, yourMove)

        points = determinePoints(yourMove, result)

        totalPoints += points

    return totalPoints

def main():
    fileOutput = []
    with open('input.txt', 'r') as file:
        fileOutput = file.readlines()

    print("Total Points = " + str(determineTotalPoints(fileOutput)))





    


