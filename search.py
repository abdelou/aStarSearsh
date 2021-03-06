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
    return [s, s, w, s, w, w, s, w]


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
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the
    nearest goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"
	frontier = util.PriorityQueue()
	
	exploredNodes = {}
    #node begin and initial state start
	
	initState = problem.getStartState()
    
    #(state - action - cost)
	beginNode = (initState, [], 0)
    
	frontier.push(beginNode, 0)
    
	while not frontier.isEmpty():
    	
		currentState, actions, currentCost = frontier.pop()
    	
		if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
    	
			exploredNodes[currentState] = currentCost
    		
			if problem.isGoalState(currentState):
				return actions
			else:
				successors = problem.getSuccessors(currentState)
    			
				for nextState, nextAction, nextCost in successors:
					newAction = actions + [nextAction]
					newCost = currentCost + nextCost
					newNode = (nextState, newAction, newCost)
					frontier.update(newNode, newCost)
	return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fifo = util.PriorityQueue()

    visitedNodes = []

    beginstate= problem.getStartState()
    firstNode = (beginstate,[], 0)

    fifo.push(firstNode,0)

    while not fifo.isEmpty():

        currentState, actions , currentCost =fifo.pop()

        currentNode =(currentState,currentCost)
        visitedNodes.append((currentState,currentCost))

        if problem.isGoalState(currentState):
            return actions
        else: 
            #liste des successeurs 
            successors = problem.getSuccessors(currentState)

            for succState ,succActions ,succCost in successors:
                updateaction= actions + [succActions]
                #updateCost = currentCost + succCost
                updateCost =problem.getCostOfActions(updateaction)
                new_node= (succState,updateaction,updateCost)

                #verifions que ce nouveau noeud optenus n'a pas deja ete explor??
                visited = False

                for nods in visitedNodes:
                    visitedstate, visitedCost= nods
                    if(succState ==visitedstate) and (updateCost >= visitedCost):
                        visited = True

                if not visited :

                    fifo.push(new_node, updateCost+heuristic(succState,problem))
                    visitedNodes.append((succState, updateCost))

    return actions



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
