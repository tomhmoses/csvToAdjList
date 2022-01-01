import csv


def convert():
    adjList = {}
    names = []

    with open('sample1.csv') as csv_file:
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
                adjList[names[line_count]] = {}
                for pos in range(len(row)):
                    if pos != 0 and row[pos]:
                        startPlace = names[line_count]
                        destinationPlace = names[pos]
                        distance = int(row[pos])
                        #print(f'Distance from {startPlace} to {destinationPlace} is {distance}')
                        adjList[names[line_count]][destinationPlace] = distance


                line_count += 1
        #print(f'Processed {line_count} lines.')
        #print(adjList)
        return adjList

if __name__ == "__main__":
    convert()