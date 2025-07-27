# %%
1. Convert List to 1D Array
Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
Expected Output:
Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]


# %%
import numpy as np
a= [12.23, 13.32, 100, 36.32]
a_1d = np.array(a)
print(a_1d)

# %% [markdown]
# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

# %%
a = np.array(range(2,11))
matrix = a.reshape(3,3)
matrix

# %% [markdown]
# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

# %%
a = np.zeros(10)
a[6] = 11
a

# %% [markdown]
# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# %%
a = np.array(range(12,38))
print(a)

# %% [markdown]
# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
# Sample output:
# Original array [1, 2, 3, 4]

# %%
a = np.array([1, 2, 3, 4]) 
a_float_type = a.astype(float)
a_float_type

arr = [1,9,7,-5,4]
b = np.array(arr, dtype=float)
b = np.asarray(arr,dtype=float)
b

# %% [markdown]
# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]

# %%
import numpy as np

fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32])
centigrade = (fahrenheit - 32) * 5/9

print("Values in Fahrenheit degrees:", np.round(fahrenheit, 2))
print("Values in Centigrade degrees:", np.round(centigrade, 2))

# %% [markdown]
# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.
# Expected Output:
# Original array: [10, 20, 30]
# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

# %%
a = np.array([10, 20, 30])
b = np.array([40,50,60,70,80,90])

result = np.append(a,b)
result

# %% [markdown]
# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

# %%
a = np.array(range(12,22))
mean = np.mean(a)
median = np.median(a)
st_deviation = np.std(a)
print(f"array = {a} mean = {mean}, median = {median} and standart deviation = {st_deviation}")

# %% [markdown]
# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

# %%
a = np.array(range(100))
arr = np.reshape(a,(10,10))
arr

# %% [markdown]
# 10 Create a 3x3x3 array with random values.

# %%
b = np.random.randint(5,10,(3,3,3))
b


