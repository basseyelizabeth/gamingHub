import random
# 1 parameter: csvFileStr (player.csv)
# returns aList (list of dictionaries containing information about each player) and header (list of keys that all
# players have)
# reads player information from a CSV file and returns a list of dictionaries containing player data and the header
def createPlayerList(csvFileStr = "players.csv"):
    aList = []
    fileObj = open(csvFileStr, "r")
    header = fileObj.readline().strip().split(",")
    for line in fileObj:
        playerDict = {}
        lineList = line.strip().split(",")
        for i in range(len(header)):
            playerDict[header[i]] = lineList[i]
        aList.append(playerDict)

    fileObj.close()

    return aList, header

# 2 parameters: dataList (aList), header
# no returns
# holds player information in file based on user input
def printPlayerInfo(dataList, header):
    fileObj = open("bassey_elizabeth.txt", "w")
    print("Each player has the following information:\n", header)
    uKey = input("Enter a key: ").lower().strip()
    while uKey not in header:
        uKey = input("Enter a key: ").lower().strip()
    for i in range(len(dataList)):
        print(dataList[i][uKey], file= fileObj)
    fileObj.close()

    print("The values have been saved to bassey_elizabeth.txt")

# 2 parameters: dataList,  keyStr (certain key in the dictionary, found in header)
# 1 return: largeValue (dictionary containing largest value)
# finds the largest value in all the players of that specific category/game
def largestValue(dataList, keyStr):
    lValue = 0

    for i in range(len(dataList)):
        if dataList[i][keyStr].isdigit() and int(dataList[i][keyStr]) > lValue:
            lValue = int(dataList[i][keyStr])
        elif not dataList[i][keyStr].isdigit():
            lValue = ""

    largeValue = {"largest": lValue}

    return largeValue

# 2 parameters: dataList,  keyStr (certain key in the dictionary, found in header)
# 1 return: smallValue (dictionary containing smallest value)
# finds the smallest value in all the players of that specific category/game
def smallestValue(dataList, keyStr):
    sValue = 10000

    for i in range(len(dataList)):
        if dataList[i][keyStr].isdigit() and int(dataList[i][keyStr]) < sValue:
            sValue = int(dataList[i][keyStr])
        elif not dataList[i][keyStr].isdigit():
            sValue = ""

    smallValue = {"smallest": sValue}

    return smallValue


# 2 parameters: dataList, rulesDictionary (dictionary containing the rules of the game)
# no returns
# allows players to choose a game and organizes outcome based on the winner
def playGame(dataList, rulesDictionary):
    chooseGame = input("Choose a game (1-2): ").strip()
    while chooseGame.isdigit() and int(chooseGame) not in range(1, 3):
        chooseGame = input("Choose a game (1-2): ").strip()
    while chooseGame.isdigit() == False:
        chooseGame = input("Choose a game (1-2): ").strip()

    player1Index = input("Choose index of player 1: ").strip()
    while (player1Index.isdigit() and int(player1Index) not in range(1, 121)) or player1Index.isdigit() == False:
        player1Index = input("Choose index of player 1: ").strip()
    player1info = dataList[int(player1Index) - 1]
    print("Player 1 is", player1info['name'])

    player2Index = input("Choose index of player 2: ").strip()
    while (player2Index.isdigit() and int(player2Index) not in range(1, 121)) or player2Index.isdigit() == False:
        player2Index = input("Choose index of player 2: ").strip()
    player2info = dataList[int(player2Index) - 1]
    print("Player 2 is", player2info['name'])

    result = ""

    if int(chooseGame) == 1:
        hitValue = rulesDictionary[1][1]
        result = playGame1(int(hitValue))
    elif int(chooseGame) == 2:
        guessNumber = rulesDictionary[2][1]
        result = playGame2(int(guessNumber))

    if result == "win":
        print(player1info['name'], "wins 10 points!")
        player1info['previous_score'] = 10
        player1info['game' + chooseGame + '_score'] = int(player1info['game' + chooseGame + '_score']) + 10
        player2info['previous_score'] = 0
    elif result == "lose":
        print(player2info['name'], "wins 10 points!")
        player2info['previous_score'] = 10
        player2info['game' + chooseGame + '_score'] = int(player2info['game' + chooseGame + '_score']) + 10
        player1info['previous_score'] = 0


# 1 parameter: hitValue (number to be addded up to)
# 1 return: "win" or "lose"
# simulates Game 1 where players randomly add numbers to reach a certain value
def playGame1(hitValue):
    print("Playing Game 1. \nNumber to aim for is", hitValue)
    p1Stop = input("Should player 1 stop? (y/n) ").strip().lower()
    while p1Stop not in ["y", "n"]:
        p1Stop = input("Should player 1 stop? (y/n) ").strip().lower()

    total = 0
    while (p1Stop != "y") and (total < hitValue):
        p1Draw = random.randint(1, 10)
        total += p1Draw
        print("Player 1 draws " + str(p1Draw) + ". Total is " + str(total) + ".")
        if total < hitValue:
            p1Stop = input("Should player 1 stop? (y/n) ").strip().lower()

    if total > hitValue:
        return "lose"
    elif total == hitValue:
        return "win"

    p2Total = 0
    while p2Total < hitValue:
        p2Draw = random.randint(1, 10)
        p2Total += p2Draw
        print("Player 2 draws " + str(p2Draw) + ". Total is " + str(p2Total) + ".")

    if p2Total == hitValue:
        return "lose"
    elif p2Total > hitValue:
        return "win"

# 1 parameter: guessNumber (number of times the hidden number is guessed)
# 1 return: "win" or "lose"
# simulates Game 2 where players guess a hidden number in a limited number of attempts
def playGame2(guessNumber):
    print("Playing Game 2.\nNumber of guesses is", guessNumber, ".\nGuess the number between 1 and 100 (inclusive).")
    hiddenNum = random.randint(1, 100)
    numGuess = 0
    average = 0
    guessedNum = []

    while numGuess < guessNumber:
        p1Guess = input("Your choice: ")
        while not (p1Guess.isdigit() == True and 1 <= int(p1Guess) <= 100):
            p1Guess = input("Your choice: ")
        guessedNum.append(int(p1Guess))

        if numGuess == 0:
            lBound = 1
            uBound = 100
        else:
            if hiddenNum < average:
                uBound = int(average)
            elif hiddenNum > average:
                lBound = int(average)

        p2Guess = random.randint(lBound, uBound)
        while p2Guess in guessedNum:
            p2Guess = random.randint(lBound, uBound)
        guessedNum.append(p2Guess)

        print("Player 2 chooses", p2Guess)
        average = (int(p1Guess) + p2Guess)/2
        if hiddenNum < average:
            print("Number is lower than the average, " + str(average) + ".")
        elif hiddenNum > average:
            print("Number is higher than the average, " + str(average) + ".")
        elif hiddenNum == average:
            print("Number is equal to the average, " + str(average) + ".")

        if p1Guess == hiddenNum:
            print("Number to guess was", hiddenNum)
            return "win"
        elif p2Guess == hiddenNum:
            print("Number to guess was", hiddenNum)
            return "lose"

        numGuess += 1

    p1Distance = abs(hiddenNum - int(p1Guess))
    p2Distance = abs(hiddenNum - p2Guess)

    print("Number to guess was", hiddenNum)

    if p1Distance < p2Distance:
        return "win"
    elif p1Distance >= p2Distance:
        return "lose"

