# code from: https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
# importing the module
import cv2
from mapper import getTownPlaces

TOWN_PLACES = getTownPlaces()
TOWN_IMAGE_LOCATIONS = {}
current = 0


def printCurrentPlace():
    print(f'please click on: {TOWN_PLACES[current]}')

# function to display the coordinates of
# of the points clicked on the image


def click_event(event, x, y, flags, params):
    global current

    # checking for left mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        current -= 1
        printCurrentPlace()

    # checking for right mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        TOWN_IMAGE_LOCATIONS[TOWN_PLACES[current]] = (x,y)
        print(TOWN_IMAGE_LOCATIONS)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, TOWN_PLACES[current],
                    (x, y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
        current += 1
        printCurrentPlace()


# driver function
if __name__ == "__main__":

    # reading the image
    img = cv2.imread('town-map-with-labels.jpeg', 1)

    # displaying the image
    cv2.imshow('image', img)

    printCurrentPlace()

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
