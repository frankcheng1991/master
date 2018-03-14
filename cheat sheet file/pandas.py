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