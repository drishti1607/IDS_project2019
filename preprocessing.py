import pandas as pd
import functools
import matplotlib.pyplot as plt

data = pd.read_csv('./cleanedData.csv')


def findClosestNeighbourhood(location, meanLocations):
    """
    Compares distances of an Airbnb at location to the mean locations
    of every neighbourhood, given by meanLocations, and assigns to its
    'neighbourhood' attribute the closest neighbourhood.
    """
    locations = list(meanLocations.keys())
    a = lambda x, y: ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5
    distances = [a(location, meanLocations[i]) for i in locations]
    return locations[distances.index(min(distances))]


def computeMeanLocations(nUnique, data, rows): 
    """
    Finds the mean locations of each neighbourhood, and returns them 
    in the form of a dict.
    """
    grpLocations = dict()
    meanLocations = dict()

    for i in nUnique:
        grpLocations[i] = []

    # Create a list of locations for each neighbourhood
    for i in range(rows):
        grpLocations[data.neighbourhood[i]].append(
            (data.latitude[i], data.longitude[i])
        )

    # Find out the mean location of each neighbourhood
    for i in nUnique:
        meanLocations[i] = (functools.reduce(
            lambda x, y: (x[0] + y[0] / len(grpLocations[i]),
            x[1] + y[1] / len(grpLocations[i])), grpLocations[i],
            (0, 0))
        )

    return meanLocations


def fillNeighbourhoodValues(data, rows):
    """
    Computes the neighbourhood to which each Airbnb with a missing
    'neighbourhood' attribute is closest to, and assigns that value
    to it.
    """
    nUnique = data.neighbourhood.unique()
    meanLocations = computeMeanLocations(nUnique, data, rows)
    # Check which rows have missing 'neighbourhood' values,
    # and fill them if missing
    for i in range(rows):
        if data.neighbourhood[i] not in nUnique:
            data.loc[i, 'neighbourhood'] = findClosestNeighbourhood(
                (data.latitude[i], data.longitude[i]),
                meanLocations
            )


def testNFillMethod(data, rows):
    """
    Tests the accuracy of the method used to fill missing values in 
    the 'neighbourhood' column.
    """
    nUnique = data.neighbourhood.unique()    
    meanLocations = computeMeanLocations(nUnique)
    computedLocations = []
    for i in range(rows):
        computedLocations.append(data.neighbourhood[i] == findClosestNeighbourhood(
                (data.latitude[i], data.longitude[i]),
                meanLocations
            ))

    print(sum(computedLocations)/len(computedLocations))



def fillMinNightValues(data, rows):
    """
    Fill in missing values in the 'minimum_nights' column.
    """
    typeUnique = data.room_type.unique()
    meanMinNights = dict()

    for i in typeUnique:
        meanMinNights[i] = [0, 0]

    data.minimum_nights.fillna(-1, inplace=True)

    for i in range(rows):
        if data.minimum_nights[i] != -1:
            meanMinNights[data.room_type[i]][0] += data.minimum_nights[i]
            meanMinNights[data.room_type[i]][1] += 1
    
    for i in typeUnique:
        meanMinNights[i][0] /= meanMinNights[i][1]

    for i in range(rows):
        if data.minimum_nights[i] == -1:
            data.loc[i, 'minimum_nights'] = round(meanMinNights[data.room_type[i]][0])


def scale(data, colsList, rows):
    """
    Scales the columns passed to ensure that each column has a mean
    of 0 and a standard deviation of 1.
    """
    mean = 0
    stdDev = 0

    for col in colsList:
        mean = sum(list(data[col]))/rows

        for i in range(rows):
            stdDev += (data[col][i] - mean)**2

        stdDev = (stdDev/(rows - 1))**0.5

        for i in range(rows):
            data.loc[i, col] = (data[col][i] - mean)/stdDev


def cleanData(data):
    """
    Drop redundant columns, clean data, and fill in missing values.
    """
    rows = data.shape[0]
    # data.drop(['name', 'host_name'], axis=1, inplace=True)
    # # Fix missing values in the last_review and reviews_per_month cols
    # data.last_review.fillna(0, inplace=True)
    # data.reviews_per_month.fillna(0, inplace=True)

    # # Fill in the missing neighbourhood values
    # fillNeighbourhoodValues(data, rows)
    # fillMinNightValues(data, rows)

    # Scale some of the numerical columns
    scale(data, ['price', 'minimum_nights', 'number_of_reviews',
        'reviews_per_month', 'availability_365'], rows)

    data.to_csv('./scaledData.csv')


cleanData(data)
