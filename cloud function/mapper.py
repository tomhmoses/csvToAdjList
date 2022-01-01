from PIL import Image, ImageDraw
from mydijkstras import Dijkstra
from scvToAdjList import convert 

SCHOOL_PLACES = ['Atrium','Biology Lab','Corridor','Dinner Hall']
SCHOOL_IMAGE_LOCATIONS = {'Atrium':(300,350),'Biology Lab':(1175,400),'Corridor':(475,700),'Dinner Hall':(1225,700)}

TOWN_PLACES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']
TOWN_IMAGE_LOCATIONS = {'A': (277, 66), 'B': (718, 65), 'C': (939, 62), 'D': (944, 220), 'E': (940, 486), 'F': (943, 641), 'G': (941, 928), 'H': (618, 935), 'I': (442, 928), 'J': (51, 931), 'K': (51, 575), 'L': (54, 297), 'M': (53, 186), 'N': (53, 60), 'O': (160, 59), 'P': (278, 196), 'Q': (279, 222), 'R': (474, 227), 'S': (724, 222), 'T': (226, 301), 'U': (475, 343), 'V': (719, 346), 'W': (231, 412), 'X': (475, 412), 'Y': (726, 489), 'Z': (444, 576), 'AA': (720, 576), 'AB': (725, 641), 'AC': (811, 752), 'AD': (443, 782), 'AE': (806, 782), 'AF': (939, 752)}


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
    dijkstras = Dijkstra(graph, start, end)
    return dijkstras.getDestinationPath()

# https://www.geeksforgeeks.org/python-pil-imagedraw-draw-line/
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
def drawPathOnImage(im, path, imageLocations, filename):
    draw = ImageDraw.Draw(im)
    for pathPart in path:
        startAndEndXYs = [imageLocations[pathPart[0]],imageLocations[pathPart[1]]]
        draw.line(startAndEndXYs, fill=(66, 135, 245,128), width=20)
        draw.line(startAndEndXYs, fill=(66, 135, 245,200), width=10)
    im.save(filename)
    return filename

def getMap(path, mapFilename, imageLocations):
    filename = "path-map.png"
    with Image.open(mapFilename) as im:
        return drawPathOnImage(im, path, imageLocations, filename)

def getClearMap(path, dimensions, imageLocations):
    filename = "/tmp/path-map.png"
    im = Image.new('RGBA', dimensions, (255, 0, 0, 0))
    return drawPathOnImage(im, path, imageLocations, filename)

def getSchoolMap(path):
    return getMap(path, "school-map.png", SCHOOL_IMAGE_LOCATIONS)

def getClearTownMap(path):
    return getClearMap(path, (1000, 1080), TOWN_IMAGE_LOCATIONS)

def getTownMap(path):
    return getMap(path, "town-map-with-labels.jpeg", TOWN_IMAGE_LOCATIONS)

def getBlankMap():
    filename = "blank-map.png"
    with Image.open("school-map.png") as im:
        im.save(filename)
    return filename

def getLabeledTownMap():
    filename = "town-map-with-labels.jpeg"
    return filename