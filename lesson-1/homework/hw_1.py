import math 
import statistics
#first assignment
a = int(input('a='))
b = int(input('b='))
p = 2*(a+b)
print("perimeter of the square =",p)
# Given diameter of circle. Find its length.
#l=2*pi*r=pi*d
d = int(input('d='))
l = round(math.pi*d,2)
print('length of the circle=',l)

# Given two numbers a and b. Find their mean.
a = int(input('a='))
b = int(input('b='))
average = statistics.mean([a+b])
print("mean of the numbers =",average)
# Given two numbers a and b. Find their sum, product and square of each number.
a = int(input('a='))
b = int(input('b='))
addition = a+b
product = a*b
square_a = math.pow(a,2)
square_b = math.pow(b,2)
print(f"the addition of the numbers ={addition},\n" 
      f"the product of the numbers ={property},\n"
      f"the square of a={square_a},\n"
      f"the square of b={square_b}")
