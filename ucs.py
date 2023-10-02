'''
@author: Devangini Patel
'''
from State import State
from Node import Node
import queue
from TreePlot import TreePlot

def performUniformCostSearch():
    """
    This method performs Uniform Cost Search
    """
    # Create priority queue
    pqueue = queue.PriorityQueue()

    # Create root node
    initialState = State()
    root = Node(initialState, None)

    # Show the search tree explored so far
    treeplot = TreePlot()
    treeplot.generateDiagram(root, root)

    # Add to priority queue
    pqueue.put((root.costFromRoot, root))  # Change from heuristic to costFromRoot

    # Keep track of visited nodes
    visited = set()

    # Check if there is something in priority queue to dequeue
    while not pqueue.empty(): 
        # Dequeue nodes from the priority queue
        _, currentNode = pqueue.get()

        # Remove from the fringe
        currentNode.fringe = False

        # Check if it has goal state
        print ("-- dequeue --", currentNode.state.place)

        # Check if this is goal state
        if currentNode.state.checkGoalState():
            print ("reached goal state")
            # Print the path
            print ("----------------------")
            print ("Path")
            currentNode.printPath()

            # Show the search tree explored so far
            treeplot = TreePlot()
            treeplot.generateDiagram(root, currentNode)
            break

        # Check if node is already visited
        if currentNode.state.place in visited:
            continue

        # Add node to visited set
        visited.add(currentNode.state.place)

        # Get the child nodes 
        childStates = currentNode.state.successorFunction()
        for childState in childStates:
            childNode = Node(State(childState), currentNode)

            # Add to tree and queue
            pqueue.put((childNode.costFromRoot, childNode))  # Change from heuristic to costFromRoot

        # Show the search tree explored so far
        treeplot = TreePlot()
        treeplot.generateDiagram(root, currentNode)

    # Print tree
    print ("----------------------")
    print ("Tree")
    root.printTree()

performUniformCostSearch()
