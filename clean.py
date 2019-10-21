import pandas as pd
import functools

data = pd.read_csv('AB_NYC.csv')
print(data)
print(data.isna().any())
col_clean = data.columns[data.isna().any()].tolist()
print(col_clean)
'''
mean_rpm = data['reviews_per_month'].mean()
data['reviews_per_month'].fillna(mean_rpm, inplace = True)
print(data)

data['last_review'].fillna(method = 'ffill', inplace = True)
print(data)

print(data.isna().any())
col_clean = data.columns[data.isna().any()].tolist()
print(col_clean)
'''
col_clean = data.columns[data.isna().any()].tolist() #gives columns which have NAN values
#print(col_clean)
cols = data
num_cols = data._get_numeric_data().columns # list of columns with numerical data
num_cols = list(set(num_cols))
# print('\n')
# print(num_cols)
cat_cols = list(set(cols) - set(num_cols)) # list of columns with categorical data
# print('\n')
# print(cat_cols)
num_cols_clean = list() #list of numeric columns to be cleaned
for i in col_clean:
    if i in num_cols:
        num_cols_clean.append(i) 
# print('\n')
# print(num_cols_clean)
cat_cols_clean = list() #list of categoric columns to be cleaned
for i in col_clean:
    if i in cat_cols:
        cat_cols_clean.append(i)
# print('\n')
# print(cat_cols_clean)
for i in num_cols_clean:
    mean_col = data[i].mean()
    data[i].fillna(mean_col, inplace = True)

for i in cat_cols_clean:
    data[i].fillna(method = 'ffill', inplace = True)

print(data)
print(data.isna().any()) #to check columns which have NAN values
col_clean = data.columns[data.isna().any()].tolist()
print(col_clean)