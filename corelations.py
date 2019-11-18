from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt
from preprocessing import computeMeanLocations 
import random
import numpy as np
from statsmodels.graphics.gofplots import qqplot
import statistics as st
import math


data = pd.read_csv('./cleanedData.csv')


# corelation between number of reviews and reviews per month
def reviews():
    reviewsTotal = data['number_of_reviews']
    reviewsPerMonth = data['reviews_per_month']
    corr, _ = pearsonr(reviewsTotal, reviewsPerMonth)
    print("Correlation between number of reviews and reviews per month")
    print('correlation coefficient: %.3f' % corr)
    print("The correlation is notable and is positive")

reviews()

def reviewsCorrelation():
    reviewsTotal = data['number_of_reviews']
    reviewsPerMonth = data['reviews_per_month']
    for i in range(int(len(reviewsTotal)/10)):
        # print(i)
        plt.scatter(reviewsTotal[i], reviewsPerMonth[i], c = "r")
    plt.show()

# reviewsCorrelation()

def coord():
    latitude = data['latitude']
    longitude = data['longitude']
    corr, _ = pearsonr(latitude, longitude)
    print("Correlation between latitude and longitude coordinates")
    print('correlation coefficient: %.3f' % corr)
    print("The correlation is not notable")

coord()

def coordCorrelation():
    latitude = data['latitude']
    longitude = data['longitude']
    for i in range(int(len(latitude)/10)):
        # print(i)
        plt.scatter(latitude[i], longitude[i], c = "r")
    plt.show()

# coordCorrelation()

def availability():
    data = pd.read_csv('./cleanedData.csv')
    nights = data['minimum_nights']
    availability = data['availability_365']
    corr, _ = pearsonr(nights, availability)
    print("Correlation between minimum number of nights and availability")
    print('correlation coefficient: %.3f' % corr)
    print("The correlation is not notable")

availability()
