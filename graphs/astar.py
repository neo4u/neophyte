from pqueue import PriorityQueue

class Graph:
    """
    Abstract graph.
    Inherit from this class and implement its methods to have a working Graph
    """
    def getChildren(self, position):
        pass

    def getHCost(self, position, goal):
        '''
        Heuristic value of a certain node. For a dijkstra implementation, return always 0
        '''
        return 0

class Node:
    def __init__(self, position, cost=0, parent=None):
        # State representation. It can be a tuple, an integer, 
        # or any data structure that holds your current state for this node
        self.position = position
        self.cost = cost
        self.parent = parent

def astar(graph, start, goal):
    # Fringe. Nodes not visited yet
    openList = PriorityQueue()

    # Visited Nodes. Each one will store it's parent position
    closedList = {}

    node = Node(start)
    openList.push(node)

    while openList:
        node, _ = openList.pop()
        position, cost = node.position, node.cost

        if position in closedList:
            # Oops. Already expanded.
            continue

        # Save the node in the closed list, and keep track of its parent
        closedList[position] = node.parent
        if position == goal:
            break
        for childPosition, actionCost in graph.getChildren(position):
            # Only add to the open list if it's not expanded yet
            if not childPosition in closedList:
                childNode = Node(childPosition, cost + actionCost, position)
                openList.push(childNode, childNode.cost + graph.getHCost(childPosition, goal))

    path = []
    if position == goal:
        # Ensure a path has been found
        path.insert(0, position)
        while position and position != start:
            position = closedList[position]
            path.insert(0, position)

    return path
