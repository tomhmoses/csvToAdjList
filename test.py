from mydijkstras import Dijkstra
from scvToAdjList import convert 

graph = convert()
print(graph)
dijkstras = Dijkstra(graph, "Biology Lab", "Dinner Hall")
print(dijkstras.getDestinationPath())
