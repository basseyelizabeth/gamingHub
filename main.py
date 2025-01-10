import helper
import user_io
# no parameters
# no returns
# calls all the functions in order and based on what the user inputs
if __name__ == '__main__':
    print("Welcome to our gaming hub!")

    aList, header = helper.createPlayerList()
    options = user_io.createOptionsDict()
    rulesDict = user_io.createRulesDict()

    userOption = ""

    while userOption != "Q":
        user_io.displayUserMenu(options)
        userOption = user_io.getUserOption(options)
        if userOption == "A":
            user_io.displayPlayerByID(aList)
        elif userOption == "B":
            helper.printPlayerInfo(aList, header)
        elif userOption == "C":
            user_io.displaySmallestValue(aList)
        elif userOption == "D":
            user_io.displayLargestValue(aList)
        elif userOption == "E":
            user_io.displayTopScores(aList)
        elif userOption == "F":
            user_io.findPlayers(aList, header)
        elif userOption == "R":
            user_io.changeRules(rulesDict)
        elif userOption == "P":
            helper.playGame(aList, rulesDict)


