import math
def minmax(currdepth, currindex, isMax):
    if currdepth == Treedepth:  
        return scores[currindex]
    if isMax:
        return max(minmax(currdepth + 1, currindex * 2, False),
                   minmax(currdepth + 1, currindex * 2 + 1, False))
    else:
        return min(minmax(currdepth + 1, currindex * 2, True),
                   minmax(currdepth + 1, currindex * 2 + 1, True))
scores = [1, 2, 3, 4]
Treedepth = math.log(len(scores), 2)
result = minmax(0, 0, True)
print(result)

        