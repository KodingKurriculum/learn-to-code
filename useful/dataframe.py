import pandas as pd

# read from excel
df = pd.read_excel('sample_data_frame.xlsx', index_col=0)
print(df)

# add a column and apply a function
df['multiple'] = df.units.apply(lambda x: 3*x)
#print(df)

# find the average
average = df['units'].mean()
#print('Average units: {0}'.format(average))