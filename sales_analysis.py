import pandas as pd
import os

# Given 12-months worth of data, I'll first merge all files
# I could get all files in a list in /Sales_Data directory using library 'os'

# gives list of CSV data files
all_files = [file for file in os.listdir('./Sales_Data')]
# print(all_files)

# to merge all files, I could read each file and place its data in a dataframe (df). Then I can 'export'
# that dataframe in a new CSV

# empty df
merged_data_df = pd.DataFrame()

# for file in all_files:
#     file_read = pd.read_csv('./Sales_Data/' + file)

#     # concat. existing df from previous-read file with new file 
#     merged_data_df=pd.concat([merged_data_df, file_read])

# all_data = merged_data_df.to_csv('all_data.csv',index=False)
print(pd.read_csv('all_data.csv').head())

# First task: Whats the best month for sales? How much was earned that month?