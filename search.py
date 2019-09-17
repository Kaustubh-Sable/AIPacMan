# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    import datetime
    startTime = datetime.datetime.now()

    fringe_list = util.Stack()
    path_explored = {}
    visited = {}

    startState = problem.getStartState()
    goalState = ()
    path_explored[startState] = [(startState, " ")]
    fringe_list.push(startState)

    while not fringe_list.isEmpty():
        top = fringe_list.pop()

        # Goal state reached
        if problem.isGoalState(top):
            goalState = top
            break

        successors = problem.getSuccessors(top)
        if top not in visited:
            visited[top] = True

        for successor in successors:
            if successor[0] not in visited:
                fringe_list.push(successor[0])
                path_explored[successor[0]] = [(top, successor[1])]

    path_directions = []
    x = path_explored[goalState]

    while (x[0][0] is not startState):
        path_directions.insert(0, x[0][1])
        x = path_explored[x[0][0]]

    path_directions.insert(0, x[0][1])

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    path_directions = list(map(lambda b: b.replace("West", w), path_directions))
    path_directions = list(map(lambda b: b.replace("East", e), path_directions))
    path_directions = list(map(lambda b: b.replace("North", n), path_directions))
    path_directions = list(map(lambda b: b.replace("South", s), path_directions))

    endTime = datetime.datetime.now()
    timeTaken = endTime - startTime

    print "\nTime taken for depth search sort: ", timeTaken.microseconds / 1000, " milliseconds"

    return path_directions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    import datetime
    startTime = datetime.datetime.now()

    path_directions = []

    startState = problem.getStartState()
    fringe_list = util.Queue()
    path_explored = {}
    visited = {}
    goalState = (-1,-1)

    path_explored[startState] = [(startState, " ")]
    fringe_list.push(startState)
    visited[startState] = True

    while not fringe_list.isEmpty():
        front = fringe_list.pop()

        if problem.isGoalState(front):
            goalState = front
            break

        successors = problem.getSuccessors(front)

        for s in successors:
            if s[0] not in visited:
                fringe_list.push(s[0])
                visited[s[0]] = True
                path_explored[s[0]] = [(front, s[1])]

    x = path_explored[goalState]

    while (x[0][0] is not startState):
        path_directions.insert(0, x[0][1])
        x = path_explored[x[0][0]]

    path_directions.insert(0, x[0][1])

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    path_directions = list(map(lambda b: b.replace("West", w), path_directions))
    path_directions = list(map(lambda b: b.replace("East", e), path_directions))
    path_directions = list(map(lambda b: b.replace("North", n), path_directions))
    path_directions = list(map(lambda b: b.replace("South", s), path_directions))

    endTime = datetime.datetime.now()
    timeTaken = endTime - startTime

    print "\nTime taken for depth search sort: ", timeTaken.microseconds / 1000, " milliseconds"

    return path_directions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    import datetime
    startTime = datetime.datetime.now()

    fringe_list = util.PriorityQueue()
    visited = []

    startState = problem.getStartState()
    fringe_list.push((startState, []), 0)

    while not fringe_list.isEmpty():
        front, directions = fringe_list.pop()

        if problem.isGoalState(front):
            break

        if front not in visited:
            successors = problem.getSuccessors(front)
            for s in successors:
                if s[0] not in visited:
                    actions = directions + [s[1]]
                    fringe_list.push((s[0],actions),problem.getCostOfActions(actions))
                    visited.append(front)


    endTime = datetime.datetime.now()
    timeTaken = endTime - startTime

    print "\nTime taken for depth search sort: ", timeTaken.microseconds / 1000, " milliseconds"

    return directions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    import datetime
    import searchAgents
    startTime = datetime.datetime.now()

    fringe_list = util.PriorityQueue()
    visited = []

    startState = problem.getStartState()
    fringe_list.push((startState, []), heuristic(startState, problem))

    while not fringe_list.isEmpty():
        top, directions = fringe_list.pop()

        # Goal state reached
        if problem.isGoalState(top):
            break

        if top not in visited:
            successors = problem.getSuccessors(top)

            for successor in successors:
                if successor[0] not in visited:
                    actions = directions + [successor[1]]
                    fringe_list.push((successor[0],actions), problem.getCostOfActions(actions) + heuristic(successor[0], problem))
                    visited.append(top)

    endTime = datetime.datetime.now()
    timeTaken = endTime - startTime

    print "\nTime taken for depth search sort: ", timeTaken.microseconds / 1000, " milliseconds"

    return directions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
