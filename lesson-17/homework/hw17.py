# %% [markdown]
# Homework 1:
# 
# import pandas as pd
# 
# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
# df = pd.DataFrame(data)
# 
# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame

# %%
import pandas as pd
import numpy as np
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [25, 30, 35, 40], 
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
        } 
df = pd.DataFrame(data)
new_df = df.rename(columns = {'First Name' : 'first name', 'Age': 'age'}                   )
print(new_df.head(3))
mean_age = new_df['age'].mean()
print(mean_age)
print(new_df[["first name",'City']])
new_df['Salary'] = np.random.randint(500,700,size=len(new_df))
print(new_df)
print(new_df.describe())

# %% [markdown]
# Homework 2:
# 
# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
# ![image.png](attachment:image.png)
# Calculate and display the maximum sales and expenses.
# Calculate and display the minimum sales and expenses.
# Calculate and display the average sales and expenses.

# %%
data = {'Month': ['Jan','Feb','Mar','Apr'],
 'Sales': [5000, 6000, 7500, 8000],
 'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)
print(sales_and_expenses)
summary = pd.DataFrame({
    'Sales':[
        sales_and_expenses['Sales'].max(),
        sales_and_expenses['Sales'].min(),
        sales_and_expenses['Sales'].mean()
        ],
    'Expenses':[
        sales_and_expenses['Expenses'].max(),
        sales_and_expenses['Expenses'].min(),
        sales_and_expenses['Expenses'].mean()
    ]}, index=['Max', 'Min', 'Mean'])

print("The summary of Sales and Expenses \n", summary )

# %% [markdown]
# Homework 3:
# 
# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
# ![image.png](attachment:image.png)
# 
# Calculate and display the maximum expense for each category.
# Calculate and display the minimum expense for each category.
# Calculate and display the average expense for each category.
# In this task, use .set_index method to make Category column as index.
# 
# Try this code, learn it and use it in the task.
# 
# expenses.set_index('Category')

# %%
data = {'Category':['Rent', 'Utilities', 'Groceries', 'Entertainment'],
        'January':[1200,200,300,150],
        'February':[1300,220,320,160],
        'March':[1400,240,330,170],
        'April':[1500,250,350,180]}
expenses = pd.DataFrame(data)
expenses.style.set_properties(**{'text-align': 'left'})
expenses = expenses.set_index('Category')

max_values = expenses.max(axis=1)
min_values = expenses.min(axis=1)
avg_values = expenses.mean(axis=1)

summary = pd.DataFrame({
    'Maximum':max_values,
    'Minimum': min_values,
    'Average': avg_values})
print("Expenses Table:\n", expenses, "\n")
print("Summary Table:\n", summary)


