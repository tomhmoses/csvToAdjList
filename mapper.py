from PIL import Image, ImageDraw

PLACES = ['Atrium','Biology Lab','Classroom','Dinner Hall']
IMAGE_LOCATIONS = {'Atrium':(300,350),'Biology Lab':(1175,400),'Classroom':(475,700),'Dinner Hall':(1225,700)}

def getPlaces():
    return PLACES

def getPath(start,end):
    return [(start,end)]

# https://www.geeksforgeeks.org/python-pil-imagedraw-draw-line/
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
def getMap(path):
    filename = "path-map.png"
    with Image.open("map.png") as im:
        draw = ImageDraw.Draw(im)
        for pathPart in path:
             draw.line([IMAGE_LOCATIONS[pathPart[0]],IMAGE_LOCATIONS[pathPart[1]]], fill=(66, 99, 245,50), width=20)
             draw.line([IMAGE_LOCATIONS[pathPart[0]],IMAGE_LOCATIONS[pathPart[1]]], fill=(66, 135, 245,128), width=10)
        im.save(filename)
    return filename

def getBlankMap():
    filename = "blank-map.png"
    with Image.open("map.png") as im:
        im.save(filename)
    return filename