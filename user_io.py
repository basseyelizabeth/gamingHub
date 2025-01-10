import helper

# 1 parameter: textFileStr ("menu_options.txt")
# 1 returns: options (dictionary that contains the possible options for the user)
# read menu options from a text file and brings out a dictionary of those options
def createOptionsDict(textFileStr = "menu_options.txt"):
    fileObj = open(textFileStr, "r")
    options = {}
    for line in fileObj:
        optionsList = line.strip().split(":")
        options[optionsList[0]] = optionsList[1]
    fileObj.close()
    return options

# 1 parameter: textFileStr ("rules.txt")
# 1 return: rulesDict (dictionary that contains the rules/parameters of the games)
# Reads game rules/parameters from a text file and brings out a dictionary of the rules
def createRulesDict(textFileStr = "rules.txt"):
    rulesDict = {}
    fileObj = open(textFileStr, "r")
    for line in fileObj:
        lineList = line.strip().split("::")
        for rules in lineList:
            rulesDict[int(lineList[0])] = [lineList[1], lineList[2]]

    return rulesDict

# 1 parameter: optionsDict (dictionary of options for the user)
# no returns
# displays the user menu of options
def displayUserMenu(optionsDict):
    for line in optionsDict:
        print(line , "->", optionsDict[line])

# 1 parameter: rulesDictionary (dictionary of rules/parameters for the game)
# no returns
# displays the game rules/parameters
def displayRules(rulesDictionary):
    for rule in rulesDictionary:
        value = rulesDictionary[rule]
        print(str(rule) + ". " + ''.join(value))
        rulesDictionary[3][1] = ' '
        rulesDictionary[4][1] = ' '

# 1 parameter: rulesDictionary
# no returns
# allows users to change the game rules/parameters in a certain bound; changes the games
def changeRules(rulesDictionary):
    print("Current game rules are:")
    displayRules(rulesDictionary)
    userChange = input("Enter a number: ").strip()
    while not (userChange.isdigit() == True and 1 <= int(userChange) <= 4):
        userChange = input("Enter a number: ").strip()
    userChange = int(userChange)


    integer = input("Choose an integer between 1-25: ").strip()
    while not (integer.isdigit() == True and 1 <= int(integer) <= 25):
        integer = input("Choose an integer between 1-25: ").strip()

    rulesDictionary[userChange][1] = integer

# 1 parameter: optionsDict
# 1 return: userOption (string that holds what the user inputs)
# receives the user's menu option based on options menu
def getUserOption(optionsDict):
    userOption = input("Option: ").strip().upper()
    while userOption not in optionsDict:
        userOption = input("Option: ").strip().upper()
    return userOption

# 1 parameter: playerDict (dictionary that holds the information of one player)
# no returns
# displays player information based on the player's dictionary
def displayPlayer(playerDict):
    print(playerDict['name'] + " [#" + playerDict['id'] + "]")
    print("\tThe game 1 score is", playerDict['game1_score'])
    print("\tThe game 2 score is", playerDict['game2_score'])
    print("\tThe game 3 score is", playerDict['game3_score'])
    totalScore = int(playerDict['game1_score']) + int(playerDict['game2_score']) + int(playerDict['game3_score'])
    print("\tThe total score is", totalScore, "\n")

# 1 parameter: dataList (list that contains many dictionaries of player information)
# no returns
# displays the player with the smallest value in a specified key
def displaySmallestValue(dataList):
    keys = ['game1_score', 'game2_score', 'game3_score']
    print("Select from this list:\n", ', '.join(keys))
    userSelect = input("Enter a key: ").lower().strip()
    while userSelect not in keys:
        userSelect = input("Enter a key: ").lower().strip()
    smallValue = helper.smallestValue(dataList, userSelect)

    for i in dataList:
        if int(i[userSelect]) == smallValue['smallest']:
            displayPlayer(i)

# 1 Parameter: dataList
# no returns
# displays the player based on their id number
def displayPlayerByID(dataList):
    userID = input("Enter the id you want to check (1-120): ").strip()
    if userID.isdigit() == True and (int(userID) >= 1 and int(userID) <= 120):
        for i in dataList:
            if i['id'] == userID:
                displayPlayer(i)
    else:
        print("Not accepted.")

# 1 parameter: dataList
# no returns
# displays the player with the largest value in a specified key
def displayLargestValue(dataList):
    keys = ['game1_score', 'game2_score', 'game3_score']
    print("Select from this list:\n", ', '.join(keys))
    userSelect = input("Enter a key: ").lower().strip()
    while userSelect not in keys:
        userSelect = input("Enter a key: ").lower().strip()
    largeValue = helper.largestValue(dataList, userSelect)

    for i in dataList:
        if int(i[userSelect]) == largeValue['largest']:
            displayPlayer(i)

# 1 parameter: dataList
# no returns
# displays the top scores from the specified list of player information
def displayTopScores(dataList):
    print("How many top scores (max is 100) do you want to display?")
    topScoreNum = input("Enter a number: ").strip()
    while not (topScoreNum.isdigit() == True and 1 <= int(topScoreNum) <= 100):
        topScoreNum = input("Enter a number: ").strip()
    topScoreNum = int(topScoreNum)

    totalScores = []
    for i in range(len(dataList)):
        playerScore = (int(dataList[i]['game1_score']) + int(dataList[i]['game2_score']) +
                       int(dataList[i]['game3_score']))
        totalScores.append(playerScore)

    totalScores.sort()
    totalScores.reverse()

    for i in range(topScoreNum):
        print(str(i+1) + ". " + str(totalScores[i]))

# 1 parameter: dataList, header
# no returns
# finds and displays players based on specified search criteria
def findPlayers(dataList, header):
    print("Each player has the following information:", header)

    uKey = input("Enter a key: ").lower().strip()
    while uKey not in header:
        uKey = input("Enter a key: ").lower().strip()

    phrase = input("Enter a search phrase: ").lower().strip()
    if not phrase.isdigit():
        phrase = phrase.capitalize()

    foundPlayers = []
    for player in dataList:
        if phrase in player[uKey].capitalize():
            foundPlayers.append(player)

    if len(foundPlayers) == 0:
        print("No player contains '" + phrase + "' in key '" + uKey + "'")
    else:
        print("Found " + str(len(foundPlayers)) + " player(s) that contain '" + phrase + "' in key '" + uKey + "'")
        for i in foundPlayers:
            displayPlayer(i)
