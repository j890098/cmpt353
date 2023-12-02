import sys
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats import multicomp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

# csvs = ['CSIL-data/c_data.csv','CSIL-data/javascript_data.csv','CSIL-data/python_data.csv','CSIL-data/java_sorts.csv']
csvs = ['data/c_data.csv','data/javascript_data.csv','data/python_data.csv','data/java_sorts.csv']
# Create an empty list to store DataFrames
dfs = []

# Loop through each file path and read the CSV into a DataFrame
for file_path in csvs:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate the DataFrames horizontally along the columns axis
result_df = pd.concat(dfs, axis=1)

# Format the column names
cols = []
count = 0
for column in result_df.columns:
    if column == 'implementedQuicksort':
        if(count == 0):
            cols.append('python_quicksort')
        else:
            cols.append('java_quicksort')
        count+=1
        continue
    cols.append(column)
result_df.columns = cols
result_df = result_df.rename(columns={"numpyBuiltin": "numpy_builtin", "java_dualqsort": "java_builtin_dualqsort"})

result_df

# Display the resulting DataFrame
print(result_df)

# Create a long-form DataFrame suitable for Tukey's test
long_form_df = result_df.melt(var_name='Algorithm', value_name='Speed (ms)')

# Perform Tukey's test
tukey_result = pairwise_tukeyhsd(long_form_df['Speed (ms)'], long_form_df['Algorithm'])

# Print the Tukey test results
print(tukey_result)

# Print some description statistics for easier comparison
description = result_df.describe()
print(description.sort_values(by = "mean", axis = 1))

# Make some Visualizations
fig, ax = plt.subplots(1, 1)
# plt.title('Histogram Of All Sorts (CSIL)')
plt.title('Histogram Of All Sorts')
ax.hist(result_df)
ax.legend((result_df.columns),loc='upper right')
# plt.savefig('CSIL-allSortsHistogramCSIL.png')
plt.savefig('allSortsHistogram.png')

dfWithoutPythonQS = result_df.drop(columns="python_quicksort")

fig, ax = plt.subplots(1, 1)
# plt.title('Histogram Without Python Quicksort (CSIL)')
plt.title('Histogram Without Python Quicksort')
ax.hist(dfWithoutPythonQS)
ax.legend((dfWithoutPythonQS.columns),loc='upper right')
# plt.savefig('CSIL-withoutPythonQuicksortHistogramCSIL.png')
plt.savefig('withoutPythonQuicksortHistogram.png')

dfWithoutJavaJavascriptPythonQS = result_df.drop(columns=["python_quicksort","java_quicksort","java_builtin_dualqsort"," javascript_quicksort"," javascript_mergesort","javascript_builtin"])

fig, ax = plt.subplots(1, 1)
# plt.title('Histogram Without java/javascript/python quicksort (CSIL)')
plt.title('Histogram Without java/javascript/python quicksort')
ax.hist(dfWithoutJavaJavascriptPythonQS)
ax.legend((dfWithoutJavaJavascriptPythonQS.columns),loc='upper right')
# plt.savefig('CSIL-withoutJavaJavascriptPythonQicksortHistogram.png')
plt.savefig('withoutJavaJavascriptPythonQicksortHistogram.png')
