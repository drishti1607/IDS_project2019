import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./cleanedData.csv')

n, bins, patches = plt.hist(data.price, 2500, facecolor='blue', alpha=0.7)

print(n)

plt.axis([0, 1000, 0, 3500])

plt.show()