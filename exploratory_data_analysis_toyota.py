import pandas as pd
from pathlib import Path
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset into a Pandas DataFrame
# The dataset is expected to be a CSV file, and its path is specified as a raw string
df = pd.read_csv(r"/kaggle/input/toyota-corolla/ToyotaCorolla.csv")

# Display the first 15 prices from the 'Price' column
# This is useful to quickly glance at some of the price values in the dataset
df['Price'][0:15]

# Display various statistics and information about the dataset
# - dtypes: shows the data type of each column
# - size: shows the total number of elements in the DataFrame
# - describe(): provides descriptive statistics of the DataFrame
df.dtypes
df.size
df.describe()

# Display statistics specifically for the 'Price' column
# This includes count, mean, std deviation, min, 25th percentile, median, 75th percentile, and max
df['Price'].describe()

# Print specific statistics for the 'Price' column
# This includes the number of rows, mean value, minimum value, and maximum value
print('Number of rows', len(df['Price']))
print('Mean value', df['Price'].mean())
print('Min in the val', df['Price'].min())
print('Max in the val', df['Price'].max())

# Rename a column from 'X' to 'Y'
# Ensure that 'X' exists in your DataFrame before running this line
df = df.rename(columns={'X': 'Y'})
df.columns

# Replace spaces in column names with underscores
# This is often done to make data handling easier, as spaces can sometimes cause issues
df.columns = [s.strip().replace(' ', '_') for s in df.columns]
df.columns

# Remove rows with any missing values (NA or NaN)
# Note: This might significantly reduce your dataset size if there are many missing values
reduced_ds = df.dropna()
print("Size was ", len(df), " and now it is ", len(reduced_ds))

# Scatter plot of Manufacturing Year vs. Price
# This can help visualize if there's a relationship or trend between the year of manufacture and the price
df.plot.scatter(x='Mfg_Year', y='Price')

# Create a series for 'Mfg_Year' and plot its histogram
# This helps visualize the distribution of manufacturing years in the dataset
ts = pd.Series(df['Mfg_Year'])
ts = ts.hist()
ts.set_xlabel('year')
ts.set_ylabel('count')
ts.plot()
