import pandas as pd
import statistics as st
from scipy import stats
from statsmodels.stats import weightstats as stests

s = """
1.  H0: Manhattan is not the most expensive part of the city
    H1: Manhattan is the most expensive part of the city
    The Null hypothesis is rejected based on the graph

2.  H0: The price of AirBnBs is unrelated to the location
    H1: The price of the AirBnBs closer to the city center is higher
    The Null hypothesis is rejected based on the graph

3.  H0: Brooklyn is not the busiest part when it comes to availability of AirBnBs
    H1: Brooklyn is the busiest part when it comes to availability of AirBnBs
    The Null hypothesis is rejected based on the graph

4.  H0: Bronx does not have the lowest number of AirBnBs
    H1: Bronx has the lowest number of AirBnBs
    The Null hypothesis is rejected based on the graph

"""

print(s)

def manhattanPrice():
    print("H0: Mean price in Manhattan is 196\nH1: Mean price in Manhattan is not 196")
    data2 = pd.read_csv('./cleanedData.csv', index_col="neighbourhood_group")
    manhattan = data2.loc[['Manhattan'],['price']]
    manhattanList = manhattan['price'].tolist()
    # print(st.mean(manhattanList))

    #price in manhattan is 200
    ztest, pval = stests.ztest(manhattanList, x2=None, value=196)
    print("p = ",float(pval))
    if pval<0.05:
        print("reject null hypothesis")
    else:
        print("accept null hypothesis")
    print("\n")

manhattanPrice()

def brooklynAvailability():
    print("H0: AirBnBs are available in Brooklyn for an average of more than 150 days out of 365")
    print("H1: AirBnBs are available in Brooklyn for an average of less than 150 days out of 365")
    m = 150
    data2 = pd.read_csv('./cleanedData.csv', index_col="neighbourhood_group")

    brooklyn = data2.loc[['Brooklyn'],['availability_365']]
    brooklynList = brooklyn['availability_365'].tolist()
    results = stats.ttest_1samp(brooklynList, m)
    alpha = 0.05
    if (results[0] < 0) & (results[1]/2 < alpha):
        print("reject null hypothesis")
    else:
        print("accept null hypothesis")
    
brooklynAvailability()