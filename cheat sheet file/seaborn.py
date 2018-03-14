import seaborn as sns

# Draw figures:
## factorplot/bar chart:
sns.factorplot(x = 'Pclass', data = titanic_df, 
	kind = 'count',hue = 'Xex') # draw on FacetGrid
## FacetGrid:
fig = sns.FacetGrid(data = 'titanic_df', hue = 'Sex',
	aspect = 4) # just create an empty grid, then add plots on it
fig.map(func = kdeplot, x = 'Age', shade = True)
	# Apply a plotting function to each facet's subset of the data.
fig.set(xlim = (0, df['a'].max())) # # Set attributes on each subplot Axes
fig.add_legend()
## lmplot(): Plot data and regression model fits across a FacetGrid: This function combines regplot() and FacetGrid
sns.lmplot(x = 'Age', y = '', data = df, hue = '',
	palette = 'winter', x_bins = [10,20,40,60,80])

# Set drawing properties:
sns.set_style('whitegrid')