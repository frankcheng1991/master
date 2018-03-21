# -*- coding: utf-8 -*-
'''
# load libs
import pandas as pd
from pandas import Series,DataFrame
from pandas.io.data import DataReader

# read files:
pd.read_csv('filename.csv')

# get properties of object create by pd
df.head()
df.info()

# functions:
pd.notnull()
df['categorical variable'].value_counts()
df['variable'].dropna()
df['a'].loc[df['a'] == 0] == 'specific value'
df['new_col'] = df['old_col'].map({0:'no', 1:'yes'}) # create new columns by mapping function

# Draw figures:
## histogram:
df['numerical variable'].hist(bins = 70)
'''

'''
url_short = https://www.tutorialspoint.com/python_pandas/index.htm
url_8books = http://www.dataschool.io/best-python-pandas-resources/
url_full = http://pandas.pydata.org/pandas-docs/version/0.17.0/pandas.pdf
url_practical = http://uweziegenhagen.de/wp-content/uploads/2016/02/Pandas.pdf
'''

# 10 Minutes for Pandas
url = http://pandas.pydata.org/pandas-docs/version/0.17.0/pandas.pdf

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# --------------------------- 10 min to learn pandas --------------------------#
## 6.1 Object Creation
# series: Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1, 3, 4, np.nan, 6, 8])
print s
# DataFrame: Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods = 6)
print dates
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list('ABCD'))
print df

df2 = pd.DataFrame({ #  by passing a dict of objects that can be converted to series-like.
		'A': 1.,
		'B': pd.Timestamp('20130102'),
		'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
		'D': np.array([3] * 4, dtype = 'int32'),
		'E': pd.Categorical(["test", "train", "test", "train"]),
		'F': 'foo'
	})
print df2
print df2.dtypes

## 6.2 Viewing Data
# See the top & bottom rows of the frame
print df.head()
print df.tail(3)
# Display the index, columns and the underlying numpy data
print df.index
print df.columns
print df.values
# Describe shows a quick statistic summary of your data
print df.describe()
# Transpose your data
print df.T
# sort by an axis
print df.sort_index(axis = 1, ascending = False) # sort by column names
# Sorting by values
print df.sort_values(by = 'B')

## 6.3 Selection
# Getting
print df['A'] # Selecting a single column, which yields a Series, equivalent to df.A
print df[0:3] # Selecting via [], which slices the rows.
print df['20130102':'20130104']
# Selection by Label (df.loc[]) --- row names of column names
print df.loc[dates[0]] # For getting a cross section using a label
print df.loc[:, ['A', 'B']] # Selecting on a multi-axis by label, this is eqyal to df[['A', 'B']]
print df.loc['20130102':'20130104', ['A', 'B']] # Showing label slicing, both endpoints are included; shape(3, 2)
print df.loc['20130102', ['A', 'B']] # Reduction in the dimensions of the returned object -> shape(2, )
print df.loc[dates[0], 'A'] # For getting a scalar value
print df.at[dates[0], 'A'] # For getting fast access to a scalar (equiv to the prior method)
# Selection by Position (df.iloc[])
print df.iloc[3] # Select via the position of the passed integers
print df.iloc[3:5, 0:2] # By integer slices, acting similar to numpy/python
print df.iloc[[1, 2, 4], [0, 2]] # By lists of integer position locations, similar to the numpy/python style
print df.iloc[1, 1] # For getting a value explicitly
print df.iat[1, 1]
# Boolean Indexing
print df[df.A > 0] 
print df[df > 0] # A where operation for getting.
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print df2[df2['E'].isin(['two', 'four'])] # Using the isin() method for filtering:
# Setting
s1 = pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20130102', periods = 6))
df['F'] = s1 # Setting a new column automatically aligns the data by the indexes
df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
print df
df2 = df.copy()
df2[df2 > 0] = -df2
print df2

## 6.4 Missing Data (np.nan)
df1 = df.reindex(index = dates[0:4], columns = list(df.columns) + ['E']) # Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.
df1.loc[dates[0]:dates[1], 'E'] = 1
print df1
print df1.dropna(how = 'any') # To drop any rows that have missing data; this is just the copy of df1, df1 itself not influenced
print df1.fillna(value = 5) # Filling missing data
print pd.isnull(df1) # To get the boolean mask where values are nan

## 6.5 Operations
# Stats: mean, shift, sub
print df.mean() # default axis = 0: columns' mean
print df.mean(1) # axis = 1: rows' mean

s = pd.Series([1, 3, 5, np.nan, 6, 8], index = dates).shift(2) # shift by 2
print s
print df.sub(s, axis = 'index')
# Apply: cumsum, lambda function
print df
print df.apply(np.cumsum) # on rows
print df.apply(lambda x: x.max() - x.min()) # on columns
# Histogramming: value_counts
s = pd.Series(np.random.randint(0, 7, size = 10))
print s.value_counts()
# String Methods: by regular expression
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print s
print s.str.lower() # it will not cause any effect on s original
print s 

## 6.6 Merge
# Concat
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]] # break into pieces
print df[3:7]
print pd.concat(pieces)
# Join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print pd.merge(left, right, on = 'key')
# Append
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
s = df.iloc[3]
print s
print df.append(s, ignore_index = True)
# grouping
'''
 group by we are referring to a process involving one or more of the following steps
. Splitting the data into groups based on some criteria
. Applying a function to each group independently
. Combining the results into a data structure
'''
df = pd.DataFrame({
		'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
		'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
		'C': np.random.randn(8),
		'D': np.random.randn(8)
	})
print df
print df.groupby('A').sum() # Grouping and then applying a function sum to the resulting groups
print df.groupby(['A', 'B']).sum() # Grouping by multiple columns forms a hierarchical index, which we then apply the function.

## 6.8 Reshaping
# Stack
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
					'foo', 'foo', 'qux', 'qux'],
					['one', 'two', 'one', 'two',
					'one', 'two', 'one', 'two']])) # zip the two columns into tuple pairs
index = pd.MultiIndex.from_tuples(tuples, names = ['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index = index, columns = ['A', 'B'])
df2 = df[:4]
print df2
stacked = df2.stack() # The stack() method "compresses" a level in the DataFrame’s columns
print stacked
print stacked.unstack() # With a “stacked” DataFrame or Series (having a MultiIndex as the index), the inverse operation of stack() is unstack(), which by default unstacks the last level:
print stacked.unstack(0) # 0 is for first index label, 1 is for second, 2 is for A and B
# Pivot Tables:
df = pd.DataFrame({
		'A': ['one', 'one', 'two', 'three'] * 3,
		'B': ['A', 'B', 'C'] * 4,
		'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
		'D': np.random.randn(12),
		'E': np.random.randn(12)
	})
print df
print pd.pivot_table(df, values = 'D', index = ['A', 'B'], columns = 'C') # We can produce pivot tables from this data very easily:

## 6.9 Time Series
# converting secondly data into 5-minutely data
rng = pd.date_range('1/1/2012', periods = 100, freq = 'S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index = rng) 
print ts.head(20)
print ts.resample('5Min', how = 'sum') # the original ts is not affected
# Time zone representation
rng = pd.date_range('3/6/2012 00:00', periods = 5, freq = 'D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print ts # this is day data
ts_utc = ts.tz_localize('UTC') 
print ts_utc
# Convert to another time zone
print ts_utc.tz_convert('US/Eastern') 
# Converting between time span representations
rng = pd.date_range('1/1/2012', periods = 5, freq = 'M')
ts = pd.Series(np.random.randn(len(rng)), index = rng)
print ts
ps = ts.to_period()
print ps
print ps.to_timestamp()
'''
Converting between period and timestamp enables some convenient arithmetic functions to be used. In the following
example, we convert a quarterly frequency with year ending in November to 9am of the end of the month following
the quarter end:
'''
prng = pd.period_range('1990Q1', '2000Q4', freq = 'Q-NOV')
print prng
ts = pd.Series(np.random.randn(len(prng)), index = prng)
print prng.asfreq('M', 'e') + 1 # change freq from 'Q-NOV' to 'M'
print (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9

## 6.10 Categoricals
df = pd.DataFrame({
		'id': [1, 2, 3, 4, 5, 6],
		'raw_grade': ['a', 'b','b', 'a', 'a', 'e']
	})
# Convert the raw grades to a categorical data type.
df['grade'] = df["raw_grade"].astype("category")
print df['grade']
# Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!)
df['grade'].cat.categories = ["very good", 'good', 'very bad']
# Reorder the categories and simultaneously add the missing categories (methods under Series .cat return a new Series per default).
df['grade'] = df['grade'].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print df['grade']
# Sorting is per order in the categories, not lexical order
print df.sort_values(by = 'grade')
# Grouping by a categorical column shows also empty categories.
print df.groupby('grade').size()

## 6.11 Plotting: index are x axis, values are y axis, columns are different lines
ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
ts = ts.cumsum()
ts.plot()
plt.show()
# On DataFrame, plot() is a convenience to plot all of the columns with labels:
df = pd.DataFrame(np.random.randn(1000, 4), index = ts.index, columns = ['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc = 'best'); plt.show()

## 6.12 Getting Data In/Out
# CSV: writing and reading csv file:
df.to_csv('foo.csv')
print pd.read_csv('foo.csv')
# HDF5
df.to_hdf('foo.h5', 'df') # writing to HDF5 store
print pd.read_hdf('foo.h5', 'df')
# Excel
df.to_excel('foo.xlsx', sheet_name = 'Sheet1') # Writing to an excel file
print pd.read_excel('foo.xlsx', 'Sheet1', index_col = None, na_values = ['NA'])

## Gotchas
# If you are trying an operation and you see an exception like:

#if pd.Series([False, True, False]):
#	print("I was True") # solution at P 281



