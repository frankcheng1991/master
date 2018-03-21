# -*- coding: utf-8 -*-
# Pandas_cookbook.py
'''
url = http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/tree/v0.1/cookbook/
'''

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.style.use('default')


#--------------------- Chap 1: Reading data from a csv file ---------------
# read data from a CSV file using the read_csv function
# original page is (in French), 
# This dataset is a list of how many people were on 7 different bike paths in Montreal, each day.

# Here is a explanation for setting path: http://kitchingroup.cheme.cmu.edu/blog/2013/06/16/Automatic-temporary-directory-changing/ 
#import os
#print os.getcwd()
#os.chdir("pandas-cookbook/data")
#print os.getcwd()

broke_df = pd.read_csv("pandas-cookbook/data/bikes.csv")
print broke_df[:3]
'''
. change the column separator to a ;
. Set the encoding to 'latin1' (the default is 'utf8')
. Parse the dates in the 'Date' column
. Tell it that our dates have the date first instead of the month first
. Set the index to be the 'Date' column
'''
fix_df = pd.read_csv('pandas-cookbook/data/bikes.csv', sep = ';', encoding = 'latin1', index_col = 'Date', dayfirst = True, parse_dates = ['Date'])
print fix_df[:3]

# Selecting a column
print fix_df['Berri 1']

# Plotting a column
fix_df['Berri 1'].plot()
plt.show()
fix_df.plot(figsize = (15, 10))
plt.show()

#--------------------- Chap 2: Selecting data & finding the most common complaint type -----------------#
# Make the graphs a bit prettier, and bigger
pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

complaint = pd.read_csv("pandas-cookbook/data/311-service-requests.csv")

# What's even in it? (the summary)¶
'''
When you look at a large dataframe, instead of showing you the contents of the dataframe, it'll show you a summary. This includes all the columns, and how many non-null values there are in each column.
'''
print complaint['Complaint Type']
print complaint['Complaint Type'][:5]
complaint['Complaint Type'][:5] # this is the same as above

# Selecting multiple columns
complaint[['Complaint Type', 'Borough']][:10]

# What's the most common complaint type?
print complaint['Complaint Type'].value_counts()
complaint_counts = complaint['Complaint Type'].value_counts()
print complaint_counts[:10]
complaint_counts[:10].plot(kind='bar')
plt.show()

#--------------------- Chap 3: Which borough has the most noise complaints? (or, more selecting data) -----------------#
noise_complaints = complaint[complaint['Complaint Type'] == "Noise - Street/Sidewalk"]
print noise_complaints[:3]
print complaint['Complaint Type'] == "Noise - Street/Sidewalk"

# This is a big array of Trues and Falses, one for each row in our dataframe. When we index our dataframe with this array, we get just the rows where.

# You can also combine more than one condition with the & operator like this:
is_noise = complaint['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaint['Borough'] == "BROOKLYN"
print complaint[is_noise & in_brooklyn][:5]