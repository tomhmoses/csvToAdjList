from PIL import Image, ImageDraw
from mydijkstras import Dijkstra
from scvToAdjList import convert 

SCHOOL_PLACES = ['Atrium','Biology Lab','Corridor','Dinner Hall']
SCHOOL_IMAGE_LOCATIONS = {'Atrium':(300,350),'Biology Lab':(1175,400),'Corridor':(475,700),'Dinner Hall':(1225,700)}

TOWN_PLACES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']

def getSchoolPlaces():
    return SCHOOL_PLACES

def getTownPlaces():
    return TOWN_PLACES

def getSchoolPath(start,end):
    graph = convert('school-graph.csv')
    dijkstras = Dijkstra(graph, start, end)
    return dijkstras.getDestinationPath()

def getTownPath(start,end):
    graph = convert('town-graph.csv', symmetrical=True)
    print(graph)
    dijkstras = Dijkstra(graph, start, end)
    return dijkstras.getDestinationPath()

# https://www.geeksforgeeks.org/python-pil-imagedraw-draw-line/
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
def getMap(path):
    filename = "path-map.png"
    with Image.open("school-map.png") as im:
        draw = ImageDraw.Draw(im)
        for pathPart in path:
            startAndEndXYs = [SCHOOL_IMAGE_LOCATIONS[pathPart[0]],SCHOOL_IMAGE_LOCATIONS[pathPart[1]]]
            draw.line(startAndEndXYs, fill=(66, 99, 245,50), width=20)
            draw.line(startAndEndXYs, fill=(66, 135, 245,128), width=10)
        im.save(filename)
    return filename

def getBlankMap():
    filename = "blank-map.png"
    with Image.open("school-map.png") as im:
        im.save(filename)
    return filename