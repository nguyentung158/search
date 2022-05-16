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

from game import Directions
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

    def getCostOfActions(self, listActions):
        """
         listActions: A list of listActions to take

        This method returns the total cost of a particular sequence of listActions.
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

    Your search algorithm needs to return a list of listActions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    startNode = problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    myStack = util.Stack()
    myVisitedNodes = []
    myStack.push((startNode,[]))
    while not myStack.isEmpty():
        currentNode, listActions = myStack.pop()
        if currentNode not in myVisitedNodes:
            myVisitedNodes.append(currentNode)
            if problem.isGoalState(currentNode):
                #print("action: ", listActions)
                return listActions
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nextAction = listActions + [action]
                myStack.push((nextNode, nextAction))
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startNode = problem.getStartState()
    if problem.isGoalState(startNode):
        return []
        
    myQueue = util.Queue()
    myVisitedNodes = []
    myQueue.push((startNode, []))

    while not myQueue.isEmpty():
        currentNode, listActions = myQueue.pop()
        if currentNode not in myVisitedNodes:
            myVisitedNodes.append(currentNode)
            if problem.isGoalState(currentNode):
                return listActions
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nextAction = listActions + [action]
                myQueue.push((nextNode, nextAction))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startNode = problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    myVisitedNodes = []
    priorityQueue = util.PriorityQueue()
    priorityQueue.push((startNode, [], 0), 0)

    while not priorityQueue.isEmpty():
        currentNode, listActions, oldCost =  priorityQueue.pop()
        if currentNode not in myVisitedNodes:
            myVisitedNodes.append(currentNode)
            if problem.isGoalState(currentNode):
                return listActions
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nextAction = listActions + [action]
                priority = oldCost + cost
                priorityQueue.push((nextNode, nextAction, priority), priority)
    """util.raiseNotDefined()"""

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startNode = problem.getStartState()
    if problem.isGoalState(startNode):
        return []

    myVisitedNodes = []

    priorityQueue = util.PriorityQueue()
    priorityQueue.push((startNode, [], 0), 0)

    while not priorityQueue.isEmpty():
        currentNode, listActions, oldCost = priorityQueue.pop()
        if currentNode not in myVisitedNodes:
            myVisitedNodes.append(currentNode)
            if problem.isGoalState(currentNode):
                return listActions
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nextAction = listActions + [action]
                newCostToNode = oldCost + cost
                heuristicCost = newCostToNode + heuristic(nextNode, problem)
                priorityQueue.push((nextNode, nextAction, newCostToNode), heuristicCost)
    """util.raiseNotDefined()"""


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
