# Exploring Data Frame Creation and Data Retrieval with Pandas

This repository contains a Jupyter Notebook that demonstrates three distinct methods to create data frames using Pandas, a powerful data manipulation and analysis library for Python. Additionally, it provides insights into data retrieval and basic statistics extraction from a dataset.

## Methods of Creating Data Frames

### 1. Manual Data Frame Creation
   - Creating a data frame by manually defining the data within the Python code.

### 2. Loading Data from a CSV File
   - Utilizing a CSV file to load data into a Pandas data frame.

### 3. Creating Data Frame from a Database
   - Forming a data frame using data fetched from a database.

## Data Retrieval Techniques

The notebook also elucidates how to retrieve specific columns and/or records from the data. For example, to extract data for specific columns like 'Id', 'Model', 'Price', 'Age_08_04', 'Mfg_Month', or to fetch records of cars with a specific attribute (e.g., cars with exactly three doors), the code can be modified accordingly.

## Extracting Data Insights

Moreover, the notebook introduces several methods to extract information related to the columns and values in a dataset:
   - `head()`: Returns the top rows of the data.
   - `columns`: Displays all column names.
   - `describe()`: Provides overall statistics for a dataset.
   - `dtypes`: Shows data types of each column.
   - `size`: Returns the size of the data frame.

## Code Snippets and Usage

## Code Snippets and Usage

### Importing Necessary Libraries
```python
import numpy as np  # For linear algebra
import pandas as pd  # For data processing, CSV file I/O
```python

### Loading Data from a CSV File

```python
df = pd.read_csv(r"/C/ToyotaCorolla.csv")
```python
### Retrieving Specific Data

```python
df['Price'] [0:15]
```python
### Extracting Data Statistics

```python
df.dtypes
df.size
df.describe()
```python


### Dataset Utilized
The dataset utilized in this notebook is related to the Toyota Corolla and is available in the /kaggle/input/toyota-corolla/ToyotaCorolla.csv path. It contains various attributes of the cars, such as 'Price', 'Age_08_04', 'Mfg_Month', and 'Doors', among others.

### Getting Started

To get started with the notebook:

Ensure that you have Jupyter Notebook installed, or use an online platform that supports it.
Clone this repository.
Navigate to the notebook and open it.
Run the cells to observe the outputs and feel free to modify the code as per your requirements.

### Contributing
Feel free to fork this repository, and contributions, issues, and feature requests are welcome!

### License
This project is open-source and available under the MIT License.

### Acknowledgements
The dataset used is from Kaggle's Toyota Corolla dataset.
The Python environment and libraries are defined by the kaggle/python Docker image.




