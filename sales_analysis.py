import pandas as pd
import os
import matplotlib.pyplot as plt

# Given 12-months worth of data, I'll first merge all files
# I could get all files in a list in /Sales_Data directory using library 'os'

# gives list of CSV data files
all_files = [file for file in os.listdir('./Sales_Data')]
# print(all_files)

# to merge all files, I could read each file and place its data in a dataframe (df). Then I can 'export'
# that dataframe in a new CSV

# empty df
# merged_data_df = pd.DataFrame()

# for file in all_files:
#     file_read = pd.read_csv('./Sales_Data/' + file)

#     # concat. existing df from previous-read file with new file 
#     merged_data_df=pd.concat([merged_data_df, file_read])

# merged_data_df.to_csv('all_data.csv',index=False)

merged_data = pd.read_csv('all_data.csv')

# First task: Whats the best month for sales? How much was earned that month?
# - get month from Order Date column in new column

# merged_data['Order Date'] = 3 # This changes the data of column 

# cleaning data
# NaN search and remove
# print(merged_data[merged_data.isna().any(axis=1)].head())
merged_data = merged_data.dropna(how='all')
# print(merged_data.head())


# add col
merged_data['Month'] = merged_data['Order Date'].str[0:2] # adding col with month: str
# literal 'Or' in Month col
merged_data = merged_data[merged_data['Month'].str[0:2] != 'Or']

# convert to int
merged_data['Month'] = merged_data['Month'].astype('int32')

# sum up prices for each month (quantity * price each)
# New method: convert to numeric for specific col
merged_data['Quantity Ordered'] = pd.to_numeric(merged_data['Quantity Ordered'])
merged_data['Price Each'] = pd.to_numeric(merged_data['Price Each'])

merged_data['Sales'] = merged_data['Quantity Ordered'] * merged_data['Price Each']


summed = merged_data.groupby('Month').sum()
# print(summed)

months = range(1,13)

plt.bar(months, summed['Sales'])
plt.xticks(months)
plt.ylabel("Sales (USD)")
plt.xlabel('Month')
# plt.show()


# Second task: What city had the highest number of sales?
# from address, we need to somehow get the cities

merged_data['city'] = merged_data['Purchase Address'].apply(lambda x: x.split(',')[1])
print(merged_data)

