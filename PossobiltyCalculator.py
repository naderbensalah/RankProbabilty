import copy


class Team:
    def __init__(self, name):
        self.name = name
        self.w = 0
        self.l = 0

    def initScore(self, MH):
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

    def getScore(self):
        return [self.name, self.w]



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


def getScores(MH,teams):
  
    for t in teams:
        t.init_scores(MH)
            
    scores = []
    for t in teams:
        scores.append(t.getScore())
    return scores    


# count the number of matches done and left to do
def checkMatches(MH):
    matches_done = 0
    matches_left = 0
    for row in MH:
        for cell in row:
            if cell == "w" or cell == "l":
                matches_done += 1
            elif cell == "":
                matches_left += 1

    print("matches done : " + str(matches_done))
    print("matches left to do : " + str(matches_left))
    print("that's " + str(pow(2, matches_left)) + " possibilities\n")
    
    return [matches_done,matches_left]


def createAllPossibilities(MH, top_n, possibilties):
    coo = emptyCellExist(MH)
    if coo[0] >= 0:

        # replace empty cells with Ws
        cp1 = copy.deepcopy(MH)
        cp1[coo[0]][coo[1]] = "w"
        createAllPossibilities(cp1, top_n, possibilties)

        # replace empty cells with Ls
        cp2 = copy.deepcopy(MH)
        cp2[coo[0]][coo[1]] = "l"
        createAllPossibilities(cp2, top_n, possibilties)
    else:

        score_board = getScores(MH,TEAMS)

        # calculate the possiblities of team making top N in the given match history
        for n in range(top_n):
            best = 0
            index = -1
            for t in range(len(score_board)):
                if best < score_board[t][1]:
                    best = score_board[t][1]
                    index = t
            # reset best team score to avoid couting it twice
            score_board[index][1] = 0
            # add 1 to the team possibilty of making top N
            possibilties[index] += 1


# return coordination of emty cell if it exists
def emptyCellExist(MH):
    for row in range(len(MH[0])):
        for cell in range(len(MH[0])):
            if MH[row][cell] == "":
                return [row, cell]
    return [-1, -1]


# top teams must be in top X
top_n = 6

# number of matches done and left to do
def calc(MH):
    matches = checkMatches(MH)

    if matches[1] > 20:
        
        return("that's way to much for me")
    else:
        # if the number of matches left to do is low enought, then start calculating the probabilities
        probabilties = [0 for a in range(len(MH[0]))]
        createAllPossibilities(MH, top_n, probabilties)
        
        for a in range(len(probabilties)):
            probabilties[a] /= pow(2, matches[1])
            probabilties[a] = int(probabilties[a] * 1000) / 10
        
        return [MH[0][1:],probabilties]
