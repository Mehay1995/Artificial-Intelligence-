##B - 351 Assignment 2
##Steven Caraher
##Written September 17, 2016
##Last Modifed September 19, 2016
##Includes:
##    Global functions to make life easier
##    Uninformed Search Package
##        (incluces makeSuccessors and uninformedSearch)
##    A* Search with heuristic
##        (includes heuristic, makeSuccessorsH, and AStarSearchOne)
##    A* Search with heuristic 2
##        (includes heuristic2, makeSuccessorsH2, and AStarSearchTwo)
##    


# PART 1:
# Let's let the 8-puzzle board be represented as an array of arrays, so that the goal
# state of the board should look like this:
# GOALSTATE = [[1,2,3],[4,5,6],[7,8," "]]
# Note that I am choosing " " to represent the blank tile
from random import randint


def arrayDoubleSwap(i1, j1, i2, j2, array):
    first = array[i1][j1]
    array[i1][j1] = array[i2][j2]
    array[i2][j2] = first
    return array


def initArray(array):
    retArray = [[9,9,9],[9,9,9],[9,9,9]]
    for i in range(0,3):
        for j in range(0,3):
            retArray[i][j] = array[i][j]
    return retArray

def printState(array):
    printString  = " "
    for i in range(0,3):
        for j in range(0,3):
            printString = " " + str(array[i][j]) + "\t"
        print(printString)
        printString = " "

def makeState(nw, n, ne, w, c, e, sw, s, se):
    array = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    array[0][0] = nw
    array[0][1] = n
    array[0][2] = ne
    array[1][0] = w
    array[1][1] = c
    array[1][2] = e
    array[2][0] = sw
    array[2][1] = s
    array[2][2] = se
    return array

GOALSTATE = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")

def testUninformedSearch(init, goal, limit):
    return uninformedSearch(goal, [init], [], limit, 0)

def testInformedSearch(init, goal, limit):
    return AStarSearchOne([[heuristic(init, goal), init]], [], goal, limit, 0)

def testInformedSearch2(init, goal, limit):
    return AStarSearchTwo([[heuristic2(init, goal), init]], [], goal, limit, 0)
    


# Successor function which creates successor without heuristic
def makeSuccessors(state):
    for i in range(0,3):
        for j in range(0,3):
            if (state[i][j] == " "):
                ith = i
                jth = j
    retStates = []
    if (ith + 1 < 3):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith + 1, jth, retArray)
        retStates.append(retArray)
    if (ith - 1 > -1):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith - 1, jth, retArray)
        retStates.append(retArray)
    if (jth + 1 < 3):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith, jth + 1, retArray)
        retStates.append(retArray)
    if (jth - 1 > -1):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith, jth - 1, retArray)
        retStates.append(retArray)
    return retStates


def uninformedSearch(goal, frontier, explored, limit, numRuns):
    if frontier == []:
        return False
    elif frontier[0] == goal:
        print("GOAL FOUND in " + str(numRuns) + " steps!")
        for i in range(0,len(explored)):
            printState(explored[i])
            print("\n\n")
        return True        
    elif limit == 0:
        print("Step limit reached. This search was not smart enough")
        return False
    else:
        subject = frontier.pop(0)
        # try a while loop while we pop to find something not in explored
        limit -= 1
        numRuns += 1
              
        if subject in explored:
            uninformedSearch(goal, frontier, explored, limit, numRuns)
        else:
            explored.append(subject)
            successors = makeSuccessors(subject)
            frontier = frontier + successors
            uninformedSearch(goal, frontier, explored, limit, numRuns)



##Heuristic Procedure
def heuristic(matrix, goal):
# Calculates how far each tile is from its goal state, and sums those distances
    sum = 0
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            tile = goal[i][j]
            for k in range(0, len(matrix)):
                for l in range(0, len(matrix)):
                    if matrix[k][l] == tile:
                        sum += (k - i) * (k - i) + (j - l) * (j - l)
    return sum


# A* With heuristic given by the homework, Successor function
# This successor function returns a data structure that looks like this:
# [ <value of f>, Board]
# Note that f = accued Costs + heuristic cost
# With will not return the states in any particular order
def makeSuccessorsH(state, accuedCost):
    for i in range(0,3):
        for j in range(0,3):
            if (state[i][j] == " "):
                ith = i
                jth = j
    retStates = []
    if (ith + 1 < 3):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith + 1, jth, retArray)
        h = heuristic(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    if (ith - 1 > -1):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith - 1, jth, retArray)
        h = heuristic(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    if (jth + 1 < 3):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith, jth + 1, retArray)
        h = heuristic(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    if (jth - 1 > -1):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith, jth - 1, retArray)
        h = heuristic(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    return retStates


# A* implementation of search using the heuristic given by homework:
# Frontier is a list of the form [ cost , state]
# explored is a list of states
# goal is a state
# limit and numRuns are both ints
def AStarSearchOne(frontier, explored, goal, limit, numRuns):
    if frontier == []:
        return False       
    elif limit == 0:
        print("Step limit reached. This search was not smart enough")
        return False
    else:
        limit -= 1
        numRuns += 1
        # subject = frontier.pop(0)
        # subject is now least-costly frontier point which has not been explored
        mini = -1
        miniIVal = 0
        for i in range(0,len(frontier)):
            if mini == -1:
                mini = frontier[i][0]
            if frontier[i][0] < mini:
                mini = frontier[i][0]
                miniIVal = i
        frontierItem = frontier.pop(miniIVal)
        subject = frontierItem[1]
        cost = frontierItem[0]
        while subject in explored:
            mini = -1
            for i in range(0,len(frontier)):
                if mini == -1:
                    mini = frontier[i][0]
                if frontier[i][0] < mini:
                    mini = frontier[i][0]
                    miniIVal = i
            frontierItem = frontier.pop(miniIVal)
            subject = frontierItem[1]
            cost = frontierItem[0]
        # Now the subject is the least-costly frontier point.
        if subject == goal:
            print("GOAL FOUND in " + str(numRuns - 1) + " steps!")
            for i in range(0,len(explored)):
                printState(explored[i])
                print("\n\n")
            return True

        else:
            explored.append(subject)
            successors = makeSuccessorsH(subject, cost)
            frontier = frontier + successors
            AStarSearchOne(frontier, explored, goal, limit, numRuns)


# here is my heuristic, which shall calculate how many items are out of place:
def heuristic2(matrix, goal):
    sum = 0
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] != goal[i][j]:
                sum = sum + 1
    return sum

def makeSuccessorsH2(state, accuedCost):
    for i in range(0,3):
        for j in range(0,3):
            if (state[i][j] == " "):
                ith = i
                jth = j
    retStates = []
    if (ith + 1 < 3):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith + 1, jth, retArray)
        h = heuristic2(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    if (ith - 1 > -1):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith - 1, jth, retArray)
        h = heuristic2(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    if (jth + 1 < 3):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith, jth + 1, retArray)
        h = heuristic2(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    if (jth - 1 > -1):
        retArray = initArray(state)
        retArray = arrayDoubleSwap(ith, jth, ith, jth - 1, retArray)
        h = heuristic2(retArray, GOALSTATE) + accuedCost
        retArray = [h] + [retArray]
        retStates.append(retArray)
    return retStates

def AStarSearchTwo(frontier, explored, goal, limit, numRuns):
    if frontier == []:
        return False       
    elif limit == 0:
        print("Step limit reached. This search was not smart enough")
        return False
    else:
        limit -= 1
        numRuns += 1
        # subject = frontier.pop(0)
        # subject is now least-costly frontier point which has not been explored
        mini = -1
        miniIVal = 0
        for i in range(0,len(frontier)):
            if mini == -1:
                mini = frontier[i][0]
            if frontier[i][0] < mini:
                mini = frontier[i][0]
                miniIVal = i
        frontierItem = frontier.pop(miniIVal)
        subject = frontierItem[1]
        cost = frontierItem[0]
        while subject in explored:
            mini = -1
            for i in range(0,len(frontier)):
                if mini == -1:
                    mini = frontier[i][0]
                if frontier[i][0] < mini:
                    mini = frontier[i][0]
                    miniIVal = i
            frontierItem = frontier.pop(miniIVal)
            subject = frontierItem[1]
            cost = frontierItem[0]
        # Now the subject is the least-costly frontier point.
        if subject == goal:
            print("GOAL FOUND in " + str(numRuns - 1) + " steps!")
            for i in range(0,len(explored)):
                printState(explored[i])
                print("\n\n")
            return True

        else:
            explored.append(subject)
            successors = makeSuccessorsH2(subject, cost)
            frontier = frontier + successors
            AStarSearchTwo(frontier, explored, goal, limit, numRuns)


initialState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")
goalState = makeState(1, 2, 3, 4, 5, 6, 7, " ", 8)
testUninformedSearch(initialState, goalState, 500)
testInformedSearch(initialState, goalState, 500)
testInformedSearch2(initialState, goalState, 500)

initialState2 = makeState(1, 2, 3, 4, 8, 5, 7, " ", 6)
initialState3 = makeState(1, 2, 3, 7, 4, 5, 8, " ", 6)
initialState4 = makeState(1, 5, 2, 4, " ", 3, 7, 8, 6)
initialState5 = makeState(7, 4, 1, 8, 5, 2, " ", 6, 3)

