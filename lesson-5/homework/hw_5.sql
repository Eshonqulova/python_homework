def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
        
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input('enter a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'this {year} is a leap year ')
else:
    print(f'this {year} is not a leap year')
##
num = int(input('Please enter a number between 1 and 100 (inclusive): '))
if num%2==1:
    print(f'{num} is not Weird!')
elif num%2==0 and 2<num<5:
    print(f'{num} is Weird!')
elif num%2==0 and 6<num<20:
    print(f'{num} is Weird!')
elif num%2==1 and num>20:
    print(f'{num} is Not Weird!')
##
a = int(input('a = '))
b = int(input('b = '))
even_num = []
if a>b:
    a, b = b, a
for i in range(a,b+1):
    if i%2==0:
        even_num.append(i)
print(even_num)
##
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = min(a, b), max(a, b)

start = a + a % 2

print(list(range(start, b + 1, 2)))
