
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.visited = False
        self.distance = None # none for infinity
        self.path = []

class Dijkstra:
    def __init__(self, graph, start, destination):
        self.graph = graph
        self.nodes = self.buildNodes()
        self.visited = {}
        self.start = self.nodes[start]
        self.destination = self.nodes[destination]
        self.current = self.start
        self.run()

    def getDestinationPath(self):
        return self.destination.path

    def buildNodes(self):
        nodes = {}
        for place, neighbors in self.graph.items():
            nodes[place] = Node(place, neighbors)
        return nodes

    def considerUnvisitedNeighbours(self):
        for neighbor, distance in self.current.neighbors.items():
            if not self.nodes[neighbor].visited:
                if self.nodes[neighbor].distance == None or self.nodes[neighbor].distance > self.current.distance + distance:
                    #set distance
                    self.nodes[neighbor].distance = self.current.distance + distance
                    #set path
                    pathToAdd = (self.current.name, self.nodes[neighbor].name)
                    prevPath = []
                    if self.current.path:
                        prevPath = self.current.path.copy()
                    self.nodes[neighbor].path = prevPath
                    self.nodes[neighbor].path.append(pathToAdd)
        self.current.visited = True

    def setNewCurrent(self):
        currentLowest = None
        for name, node in self.nodes.items():
            # print(f'testing: {node.name}')
            if not node.visited and (node.distance or node.distance == 0) and (currentLowest == None or node.distance < currentLowest.distance):
                currentLowest = node
        self.current = currentLowest

    def run(self):
        self.start.distance = 0
        while not self.destination.visited:
            self.setNewCurrent()
            self.considerUnvisitedNeighbours()