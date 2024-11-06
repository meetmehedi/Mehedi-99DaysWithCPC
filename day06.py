import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

print("Dataset Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())
print("\nValue Counts for Categorical Columns:")
print(df['sex'].value_counts())
print(df['class'].value_counts())
print("\nMissing Values:\n", df.isnull().sum())

survival_summary = df.groupby('survived').mean()
print("Survival Statistics:\n", survival_summary)

sns.countplot(data=df, x='sex', hue='survived')
plt.title('Survival by Gender')
plt.show()

sns.countplot(data=df, x='class', hue='survived')
plt.title('Survival by Passenger Class')
plt.show()

sns.histplot(data=df, x='age', hue='survived', multiple='stack', kde=True)
plt.title('Age Distribution by Survival')
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()