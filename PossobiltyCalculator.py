import copy
from TeamsData import MATCH_HISTORY
from TeamsData import getScores,checkMatches


def createAllPossibilities(MH, topN, possibilties):
    coo = emptyCellExist(MH)
    if coo[0] >= 0:

        # replace empty cells with Ws
        cp1 = copy.deepcopy(MH)
        cp1[coo[0]][coo[1]] = "w"
        createAllPossibilities(cp1, topN, possibilties)

        # replace empty cells with Ls
        cp2 = copy.deepcopy(MH)
        cp2[coo[0]][coo[1]] = "l"
        createAllPossibilities(cp2, topN, possibilties)
    else:

        score_board = getScores(MH)
        
        # calculate the possiblities of team making top N in the given match history
        for n in range(topN):
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
topN = 6

#number of matches done and left to do
matches=checkMatches(MATCH_HISTORY)

if matches[1] > 20:
    print("that's way to much for me")
else:
    # if the number of matches left to do is low enought, then start calculating the probabilities
    probabilties = [0 for a in range(len(MATCH_HISTORY[0]))]
    createAllPossibilities(MATCH_HISTORY, topN, probabilties)

    print(MATCH_HISTORY[0][1:])
    for a in range(len(probabilties)):
        probabilties[a] /= pow(2, matches[1]) 
        probabilties[a] = int(probabilties[a] * 1000) / 10
    print(probabilties)
