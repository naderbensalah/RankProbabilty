class Team:
    def __init__(self, name):
        self.name = name
        self.w = 0
        self.l = 0

    def init_scores(self, MH):
        for rowIndex in range(0, len(MH[0])):
            if MH[rowIndex][0] == self.name:
                index = rowIndex
        for columnIndex in range(0, len(MH[0])):
            result = MH[columnIndex][index]
            if result == "w":
                self.l += 1
            elif result == "l":
                self.w += 1

        for columnIndex in range(0, len(MH[0])):
            if MH[0][columnIndex] == self.name:
                index = columnIndex
        for rowIndex in range(0, len(MH[0])):
            result = MH[index][rowIndex]
            if result == "w":
                self.w += 1
            elif result == "l":
                self.l += 1

    def toString(self):
        r = "| " + self.name.ljust(9) + "|\n"
        r += "|" + "----------" + "|\n"
        r += "| w: " + str(self.w).ljust(6) + "|\n"
        r += "| l: " + str(self.l).ljust(6) + "|\n"
        return r

    def getScore(self):
        return [self.name, self.w]


# current score
MATCH_HISTORY = [
    ["X", "RGE", "VIT", "G2", "MSF", "AST", "MAD", "FNC", "SK", "XL", "BDS"],
    ["RGE", "X", "w", "w", "l", "l", "w", "l", "l", "w", ""],
    ["VIT", "w", "X", "l", "w", "l", "w", "l", "w", "w", ""],
    ["G2", "w", "l", "X", "w", "w", "l", "l", "w", "w", ""],
    ["MSF", "w", "l", "v", "X", "w", "w", "l", "w", "w", ""],
    ["AST", "l", "l", "l", "l", "X", "l", "l", "l", "", ""],
    ["MAD", "w", "l", "v", "w", "l", "X", "l", "l", "", ""],
    ["FNC", "l", "l", "l", "w", "l", "l", "X", "w", "", ""],
    ["SK", "w", "l", "w", "l", "w", "w", "l", "X", "", ""],
    ["XL", "w", "l", "w", "w", "l", "l", "w", "w", "X", ""],
    ["BDS", "w", "l", "w", "w", "l", "w", "w", "l", "", "X"],
]

def createTeams():
    Teams = []
    Teams.append(Team("RGE"))
    Teams.append(Team("VIT"))
    Teams.append(Team("G2"))
    Teams.append(Team("MSF"))
    Teams.append(Team("AST"))
    Teams.append(Team("MAD"))
    Teams.append(Team("FNC"))
    Teams.append(Team("SK"))
    Teams.append(Team("XL"))
    Teams.append(Team("BDS"))
    return Teams

TEAMS = createTeams()


def getScores(MH):
    global TEAMS    
    for t in TEAMS:
        t.init_scores(MH)
            
    scores = []
    for t in TEAMS:
        scores.append(t.getScore())
    return scores    


# count the number of matches done and left to do
def checkMatches(MH):
    matchesDone = 0
    matchesLeft = 0
    for row in MH:
        for cell in row:
            if cell == "w" or cell == "l":
                matchesDone += 1
            elif cell == "":
                matchesLeft += 1

    print("matches done : " + str(matchesDone))
    print("matches left to do : " + str(matchesLeft))
    print("that's " + str(pow(2, matchesLeft)) + " possibilities\n")
    
    return [matchesDone,matchesLeft]
