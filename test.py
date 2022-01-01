from mydijkstras import Dijkstra
from scvToAdjList import convert, getPlaces

graph = convert('school-graph.csv')
print(graph)
dijkstras = Dijkstra(graph, "Biology Lab", "Dinner Hall")
print(dijkstras.getDestinationPath())

print(getPlaces('town-graph.csv'))