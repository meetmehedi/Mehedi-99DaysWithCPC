import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('supermarket_sales.csv')

print("First five rows of the dataset:")
print(data.head())

print("\nMissing values per column:")
print(data.isnull().sum())

print("\nSummary statistics for numerical columns:")
print(data.describe())

data.dropna(inplace=True)

branch_sales = data.groupby('Branch')['Total'].sum()
print("\nTotal sales by branch:")
print(branch_sales)

avg_rating = data.groupby('Branch')['Rating'].mean()
print("\nAverage rating per branch:")
print(avg_rating)

gender_sales = data.groupby('Gender')['Total'].sum()
print("\nTotal sales by gender:")
print(gender_sales)

payment_types = data['Payment'].value_counts()
print("\nPayment method distribution:")
print(payment_types)

plt.figure(figsize=(8, 6))
branch_sales.plot(kind='bar', color='skyblue', title='Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()

plt.figure(figsize=(8, 6))
gender_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, title='Sales by Gender')
plt.ylabel('') 
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Payment', data=data, palette='viridis')
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.show()

print("\n Summary of Findings ")
print("1. Total sales are highest in Branch A/B/C (customize with branch with highest sales).")
print("2. Average customer ratings are highest in Branch X.")
print("3. Sales by gender show that Male/Female customers contributed more.")
print("4. Preferred payment method is Credit Card/E-Wallet/Cash.")