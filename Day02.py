import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('supermarket_sales.csv')
print(data.head())
print(data.isnull().sum())
data.dropna(inplace=True)

branch_sales = data.groupby('Branch')['Total'].sum()
avg_rating = data.groupby('Branch')['Rating'].mean()
gender_sales = data.groupby('Gender')['Total'].sum()
payment_types = data['Payment'].value_counts()

print("\nTotal sales by branch:\n", branch_sales)
print("\nAverage rating per branch:\n", avg_rating)
print("\nTotal sales by gender:\n", gender_sales)
print("\nPayment method distribution:\n", payment_types)

plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
branch_sales.plot(kind='bar', title='Total Sales by Branch')
plt.subplot(1, 3, 2)
gender_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Gender')
plt.subplot(1, 3, 3)
sns.countplot(x='Payment', data=data).set_title('Payment Method Distribution')
plt.tight_layout()
plt.show()