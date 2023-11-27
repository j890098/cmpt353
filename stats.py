import sys
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats import multicomp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

csvs = ['c_data.csv','javascript_data.csv','python_data.csv']
# Create an empty list to store DataFrames
dfs = []

# Loop through each file path and read the CSV into a DataFrame
for file_path in csvs:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate the DataFrames horizontally along the columns axis
result_df = pd.concat(dfs, axis=1)

# Display the resulting DataFrame
print(result_df)

# Create a long-form DataFrame suitable for Tukey's test
long_form_df = result_df.melt(var_name='Algorithm', value_name='Speed (ms)')

# Perform Tukey's test
tukey_result = pairwise_tukeyhsd(long_form_df['Speed (ms)'], long_form_df['Algorithm'])

# Print the Tukey test results
print(tukey_result)