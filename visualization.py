import pandas as pd
import matplotlib.pyplot as plt
from preprocessing import computeMeanLocations 
import random
import numpy as np
from statsmodels.graphics.gofplots import qqplot
import statistics as st
import math


data = pd.read_csv('./scaledData.csv', index_col="neighbourhood")
data1 = pd.read_csv('./scaledData.csv')

"""
n, bins, patches = plt.hist(data.price, 2500, facecolor='blue', alpha=0.7)

print(n)

plt.axis([0, 1000, 0, 3500])

plt.show()
"""


# A scatter plot showing the mean rentals of AirBnBs in each neighbourhood, with each point located according to the mean location of AirBnBs in that neighbourhood
def neighbourhoodPricePlot():
    nList = list(set(data1['neighbourhood']))
    nPriceDict = dict()
    nPriceList = []
    meanPrice = 0
    for i in nList:
        nPrice = data.loc[[i],['price']]
        nPriceList = nPrice['price'].tolist()
        for j in nPriceList:
            meanPrice += j
        meanPrice /= len(nPriceList)
        nPriceDict[i] = meanPrice

    meanPrice = 0
    for i in nPriceDict.values():
        meanPrice += i
    meanPrice /= len(nPriceDict)

    rows = data1.shape[0]
    meanLocationDict = computeMeanLocations(nList, data1, rows)

    xValue = []
    yValue = []
    c = "black"
    data2 = pd.read_csv('./scaledData.csv', index_col="neighbourhood_group")
    brooklyn = data2.loc[['Brooklyn'],['neighbourhood']]
    brooklynList = list(set(brooklyn['neighbourhood'].tolist()))
    # print(len(brooklynList))
    manhattan = data2.loc[['Manhattan'],['neighbourhood']]
    manhattanList = list(set(manhattan['neighbourhood'].tolist()))
    # print(len(manhattanList))
    staten = data2.loc[['Staten Island'],['neighbourhood']]
    statenList = list(set(staten['neighbourhood'].tolist()))
    queens = data2.loc[['Queens'],['neighbourhood']]
    queensList = list(set(queens['neighbourhood'].tolist()))
    # print(len(queensList))
    bronx = data2.loc[['Bronx'],['neighbourhood']]
    bronxList = list(set(bronx['neighbourhood'].tolist()))
    #print(len(bronxList))

    for i in meanLocationDict:
        # print(i)
        size = nPriceDict[i]/meanPrice
        '''
        if i in brooklynList:
            c = "r"
        elif i in manhattanList:
            c = "y"
        elif i in queensList:
            c = "b"
        elif i in bronxList:
            c = "g"
        elif i in statenList:
            c = "k"
        '''
        xValue.append(meanLocationDict[i][0])
        yValue.append(meanLocationDict[i][1])
        plt.scatter(xValue, yValue, color = c, s = abs(size)*2, alpha = 0.3) 
    
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Location of neighbourhood groups with size of point proportional to the average price')
    plt.show()

# neighbourhoodPricePlot()


# bar chart giving number of airBnBs in each neighbourhood group
def airBnBinEachNeighbourhood():
    brooklynCount = 0
    manhattanCount = 0
    queensCount = 0
    bronxCount = 0
    statenCount = 0
    for i in data['neighbourhood_group']:
        if i == 'Brooklyn':
            brooklynCount+=1
        elif i == 'Manhattan':
            manhattanCount+=1
        elif i == 'Queens':
            queensCount+=1
        elif i == 'Bronx':
            bronxCount+=1
        elif i == 'Staten Island':
            statenCount+=1
    objects = ('Manhattan','Brooklyn','Queens','Bronx','Staten Island')
    print(objects)
    x = np.arange(len(objects))
    y = [manhattanCount, brooklynCount, queensCount, bronxCount, statenCount]
    print(y)
    plt.bar(x, y, align='center', alpha=0.5)
    plt.xticks(x, objects)
    plt.xlabel('Neighbourhood groups')
    plt.ylabel('Number of AirBnBs')
    plt.title('Number of AirBnBs in each neighbourhood group')
    plt.show()

# airBnBinEachNeighbourhood()


# bar chart with pricing of different rooms in different neighbourhood groups

def priceRoomNeighbourhood():
    groups = 5
    data2 = pd.read_csv('./cleanedData.csv', index_col="neighbourhood_group")

    brooklyn = data2.loc[['Brooklyn'],['room_type','price']]
    brooklynDict = {'Private room': [], 'Entire home/apt': [], 'Shared room': []}
    brooklynPrice = brooklyn['price'].tolist()
    brooklynRoom = brooklyn['room_type'].tolist()
    j = 0
    for i in brooklynRoom:
        if i == 'Private room':
            brooklynDict['Private room'].append(brooklynPrice[j])
        elif i == 'Entire home/apt':
            brooklynDict['Entire home/apt'].append(brooklynPrice[j])
        elif i == 'Shared room':
            brooklynDict['Shared room'].append(brooklynPrice[j])
        j+=1

    manhattan = data2.loc[['Manhattan'],['room_type','price']]
    manhattanDict = {'Private room': [], 'Entire home/apt': [], 'Shared room': []}
    manhattanPrice = manhattan['price'].tolist()
    manhattanRoom = manhattan['room_type'].tolist()
    j = 0
    for i in manhattanRoom:
        if i == 'Private room':
            manhattanDict['Private room'].append(manhattanPrice[j])
        elif i == 'Entire home/apt':
            manhattanDict['Entire home/apt'].append(manhattanPrice[j])
        elif i == 'Shared room':
            manhattanDict['Shared room'].append(manhattanPrice[j])
        j+=1

    queens = data2.loc[['Queens'],['room_type','price']]
    queensDict = {'Private room': [], 'Entire home/apt': [], 'Shared room': []}
    queensPrice = queens['price'].tolist()
    queensRoom = queens['room_type'].tolist()
    j = 0
    for i in queensRoom:
        if i == 'Private room':
            queensDict['Private room'].append(queensPrice[j])
        elif i == 'Entire home/apt':
            queensDict['Entire home/apt'].append(queensPrice[j])
        elif i == 'Shared room':
            queensDict['Shared room'].append(queensPrice[j])
        j+=1

    bronx = data2.loc[['Bronx'],['room_type','price']]
    bronxDict = {'Private room': [], 'Entire home/apt': [], 'Shared room': []}
    bronxPrice = bronx['price'].tolist()
    bronxRoom = bronx['room_type'].tolist()
    j = 0
    for i in bronxRoom:
        if i == 'Private room':
            bronxDict['Private room'].append(bronxPrice[j])
        elif i == 'Entire home/apt':
            bronxDict['Entire home/apt'].append(bronxPrice[j])
        elif i == 'Shared room':
            bronxDict['Shared room'].append(bronxPrice[j])
        j+=1
    
    staten = data2.loc[['Staten Island'],['room_type','price']]
    statenDict = {'Private room': [], 'Entire home/apt': [], 'Shared room': []}
    statenPrice = staten['price'].tolist()
    statenRoom = staten['room_type'].tolist()
    j = 0
    for i in statenRoom:
        if i == 'Private room':
            statenDict['Private room'].append(statenPrice[j])
        elif i == 'Entire home/apt':
            statenDict['Entire home/apt'].append(statenPrice[j])
        elif i == 'Shared room':
            statenDict['Shared room'].append(statenPrice[j])
        j+=1

    # Brooklyn, Manhattan, Queens, Bronx, Staten Island
    pricePvtRoom = [ st.mean(manhattanDict['Private room']), st.mean(brooklynDict['Private room']), st.mean(queensDict['Private room']), st.mean(bronxDict['Private room']), st.mean(statenDict['Private room'])]
    priceEntire = [st.mean(manhattanDict['Entire home/apt']), st.mean(brooklynDict['Entire home/apt']), st.mean(queensDict['Entire home/apt']), st.mean(bronxDict['Entire home/apt']), st.mean(statenDict['Entire home/apt'])]
    priceShare = [st.mean(manhattanDict['Shared room']), st.mean(brooklynDict['Shared room']), st.mean(queensDict['Shared room']), st.mean(bronxDict['Shared room']), st.mean(statenDict['Shared room'])]
    
    fig, ax = plt.subplots()
    index = np.arange(groups)
    bar_width = 0.25
    opacity = 0.8

    bar1 = plt.bar(index, pricePvtRoom, bar_width, alpha=opacity, color='b', label='Private Rooms')
    bar2 = plt.bar(index + bar_width, priceEntire, bar_width, alpha=opacity, color='g', label='Entire Room/Apt')
    bar3 = plt.bar(index + 2*bar_width, priceShare, bar_width, alpha=opacity, color='y', label='Shared rooms')

    plt.xlabel('Neighbourhood groups')
    plt.ylabel('Prices')
    plt.title('Prices of rooms in each neighbourhood group')
    plt.xticks(index + bar_width, ('Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'))
    plt.legend()    

    plt.tight_layout()
    plt.show()
    
# priceRoomNeighbourhood()


# distance from city center vs price

def distancePrice():
    data2 = pd.read_csv('./cleanedData.csv')
    newYork = (40.730610, -73.935242)
    prices = data2['price'].tolist()
    latitude = data2['latitude'].tolist()
    longitude = data2['longitude'].tolist()
    # distanceFromCenter = []
    area = np.pi*3
    print(range(len(latitude)))
    for i in range(int(len(latitude))):
        x = latitude[i] - newYork[0]
        y = longitude[i] - newYork[1]
        distance = math.sqrt(x*x + y*y)
        # distanceFromCenter.append(distance)
        print(i)
        plt.scatter(distance, prices[i], s = area*2, c = "black", alpha = 0.5)
    plt.xlabel('Distance from city center')
    plt.ylabel('Prices')
    plt.title('Prices of rooms vs distance from city center')
    plt.show()
    

# distancePrice()


# availability and area

def nightsReview():
    data2 = pd.read_csv('./cleanedData.csv', index_col="neighbourhood_group")

    brooklyn = data2.loc[['Brooklyn'],['availability_365']]
    brooklynList = brooklyn['availability_365'].tolist()
    brooklynMean = st.mean(brooklynList)

    manhattan = data2.loc[['Manhattan'],['availability_365']]
    manhattanList = manhattan['availability_365'].tolist()
    manhattanMean = st.mean(manhattanList)

    staten = data2.loc[['Staten Island'],['availability_365']]
    statenList = staten['availability_365'].tolist()
    statenMean = st.mean(statenList)

    queens = data2.loc[['Queens'],['availability_365']]
    queensList = queens['availability_365'].tolist()
    queensMean = st.mean(queensList)

    bronx = data2.loc[['Bronx'],['availability_365']]
    bronxList = bronx['availability_365'].tolist()
    bronxMean = st.mean(bronxList)

    # print(brooklynMean, manhattanMean, statenMean, queensMean, bronxMean)
    objects = ('Manhattan', 'Brooklyn', 'Staten Island', 'Queens', 'Bronx')
    y_pos = np.arange(len(objects))
    availability = [manhattanMean, brooklynMean, statenMean, queensMean, bronxMean]
    plt.barh(y_pos, availability, align = "center", alpha = 0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Availability in one year')
    plt.title('Average number of days available in a year')

    plt.show()

# nightsReview()


