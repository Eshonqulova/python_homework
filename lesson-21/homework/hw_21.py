import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1['Average grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)
max_grade = df1['Average grade'].max()
df1['Top average grade'] = max_grade
print(df1)
avg_subjects = df1[['Math', 'English', 'Science']].mean()
plt.bar(avg_subjects.index, avg_subjects.values)
plt.title('Average grade by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average grade')
plt.ylim(0, 100)
plt.show()

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
Total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print(Total_sales)
df2['Total sales by products'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
top_sale_row = df2[df2['Total sales by products'] == df2['Total sales by products'].max()]
top_sale_info = top_sale_row[['Date', 'Total sales by products']].rename(columns={'Total sales by products': 'the top sales'})
print(top_sale_info)
pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print(pct_change)
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='^')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='*')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='+')
plt.title('Sales trends over time', color='red')
plt.xlabel('Date', color='red')
plt.ylabel('Sales', color='red')
plt.ylim(0, 200)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=30)
plt.yticks(rotation=45)
plt.show()

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)
top_experience = df3[df3['Experience (Years)'] == df3['Experience (Years)'].max()]
top_experience_renamed = top_experience[['Employee_ID', 'Name', 'Experience (Years)']].rename(columns={'Experience (Years)': 'Top experience year'})
print(top_experience_renamed)
df3['Salary Increase'] = df3['Salary'].max() / df3['Salary'].min()
print(df3)
dep_counts = df3['Department'].value_counts()
dep_counts.plot(kind='bar', color='blue')
plt.title('The distribution of employees across different departments',
          color='darkblue',
          fontsize=16,
          fontweight='bold')
plt.xlabel('Department', color='blue', fontweight='bold', fontsize=12)
plt.xticks(rotation=0)
plt.ylabel('Number of employees', color='blue', fontweight='bold', fontsize=12)
plt.show()

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
total_revenue = df4['Total_Price'].sum()
print(f"Total revenue: {total_revenue}")
counting = df4['Product'].value_counts()
top_product = counting.idxmax()
top_count = counting.max()
print(f"Most ordered product: {top_product} ({top_count} orders)")
avg_quantity = df4.groupby('Product')['Quantity'].mean()
print(avg_quantity)
sales_by_product = df4.groupby("Product")['Total_Price'].sum()
sales_by_product.plot(kind='pie', autopct='%1.1f%%')
plt.xlabel('Product', color='darkblue', fontweight='normal', fontstyle='italic', fontsize=12)
plt.ylabel('Total_Price', color='darkblue', fontweight='normal', fontstyle='italic', fontsize=12)
plt.title("The distribution of sales across different products",
          color='darkblue', fontweight='normal', fontstyle='italic', fontsize=16)
plt.show()
