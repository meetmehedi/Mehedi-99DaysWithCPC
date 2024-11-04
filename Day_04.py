import pandas as pd
import numpy as np

df = pd.read_csv('your_dataset.csv')

print("First 5 rows of the dataset:")
print(df.head())
print("\nDataFrame Info:")
print(df.info())

df.dropna(inplace=True)

statistics = {
    'Mean': df.mean(),
    'Median': df.median(),
    'Mode': df.mode().iloc[0], 
    'Standard Deviation': df.std(),
    'Variance': df.var(),
    'Min': df.min(),
    'Max': df.max(),
}
stats_df = pd.DataFrame(statistics)

print("\nKey Statistics:")
print(stats_df)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['column_name'], bins=30, kde=True)
plt.title('Distribution of column_name')
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.show()