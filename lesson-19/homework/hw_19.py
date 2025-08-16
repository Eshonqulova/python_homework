import pandas as pd
df = pd.read_csv('sales_data.csv')
df.head()

Total_quantity_sold = df.groupby(['Category']).agg({"Quantity":['sum', 'max'], 'Price':'mean'})
Total_quantity_sold

Total_quantity_sold = df.groupby(['Category','Date'])["Quantity"].sum().reset_index()
top_products = Total_quantity_sold.sort_values('Quantity', ascending=False).groupby('Category').first().reset_index()
top_products

df['Total'] = df['Quantity']*df['Price']
daily_sales =  df.groupby('Date')['Total'].sum().reset_index()
Max_sales_date = daily_sales.loc[daily_sales['Total'].idxmax()]
print("Eng katta savdo bo'lgan sana:")
print(Max_sales_date)

import pandas as pd
dt_customers = pd.read_csv("customer_orders.csv")
dt_customers

grouped_dt = dt_customers.groupby('CustomerID').filter(lambda x: len(x)<20)
len(grouped_dt)
grouped_dt

dt_customers['Unit price'] = dt_customers['Price']/dt_customers['Quantity']
mean_values = dt_customers.groupby('CustomerID')['Unit price'].mean()
filter_values = mean_values[mean_values>120]
filtered_df = filter_values.reset_index(name='Avg Unit Price')
filtered_df

product_summary = (
    dt_customers.groupby('Product', as_index=False).
        agg(
            Total_quantity =('Quantity','sum'),
            Total_price = ('Price','sum')
            )
            )
filtered_product = product_summary[product_summary['Total_quantity']<5]
filtered_product

import sqlite3
import pandas as pd

import pandas as pd
import sqlite3

# Bazadan o‘qish
conn = sqlite3.connect("C:\\MY_PROJECTS\\MAAB_python\\2nd_python\\population.db")
df = pd.read_sql("SELECT Salary FROM population", conn)

# Excel fayldagi bandlarni olish
bands = [
    (0, 200000, "till $200,000"),
    (200001, 400000, "$200,001 - $400,000"),
    (400001, 600000, "$400,001 - $600,000"),
    (600001, 800000, "$600,001 - $800,000"),
    (800001, 1000000, "$800,001 - $1,000,000"),
    (1000001, 1200000, "$1,000,001 - $1,200,000"),
    (1200001, 1400000, "$1,200,001 - $1,400,000"),
    (1400001, 1600000, "$1,400,001 - $1,600,000"),
    (1600001, 1800000, "$1,600,001 - $1,800,000"),
    (1800001, 10**9, "$1,800,001 and over"),
]

# Har bir band bo‘yicha hisoblash
rows = []
total = len(df)

for low, high, name in bands:
    group = df[(df["salary"] >= low) & (df["salary"] <= high)]
    rows.append({
        "Salary Band": name,
        "Percentage": round(len(group) / total * 100, 2),
        "Average Salary": group["salary"].mean(),
        "Median Salary": group["salary"].median(),
        "Number of population": len(group)
    })

# DataFrame qilib yozish
result = pd.DataFrame(rows)

# Excelga yozish
result.to_excel("C:\\MY_PROJECTS\\MAAB_python\\2nd_python\\population_salary_analysis_filled.xlsx", index=False)

print(result)




