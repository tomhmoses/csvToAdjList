import csv

def getPlaces(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            names = row
            return names
    

def convert(filename, symmetrical = False):
    adjList = {}
    names = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # if first line
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                #print(row)
                # save names for all places
                names = row
                line_count += 1
            
            # if a line of distances
            else:
                #print(row)
                startPlace = names[line_count]
                if startPlace not in adjList:
                    adjList[startPlace] = {}
                for pos in range(len(row)):
                    if pos != 0 and row[pos] and int(row[pos]) > 0:
                        destinationPlace = names[pos]
                        distance = int(row[pos])
                        #print(f'Distance from {startPlace} to {destinationPlace} is {distance}')
                        adjList[startPlace][destinationPlace] = distance
                        if symmetrical:
                            if destinationPlace not in adjList:
                                adjList[destinationPlace] = {}
                            adjList[destinationPlace][startPlace] = distance
                line_count += 1
        return adjList

if __name__ == "__main__":
    convert()