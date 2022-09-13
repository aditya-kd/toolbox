from heapq import merge


def solve(coordinates):
    ranegsum = 0
    coordinates.sort()

    mergedCoordinates = []
    start = coordinates[0][0]
    end = coordinates[0][1]

    for i in range(1, len(coordinates)):
        currstart = coordinates[i][0]
        currend = coordinates[i][1]
        if currstart<= end:
            end = max(currend, end)

        else:
            mergedCoordinates.append([start, end])
            start = currend
            end = currend

    mergedCoordinates.append([start, end])
    for rng in mergedCoordinates:
        rangesum+= rng[i] - rng[0] +1
    
    return rangesum
