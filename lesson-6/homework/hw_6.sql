#1. 
text = 'abcabcabcdabcdabcdef'
i = 2
vowels = ['a','o','e','i','u']
while i < len(text)-1:
    if text[i] not in vowels:
        text = text[:i+1]+'_'+text[i+1:]
        vowels.append(text[i])
        i+=4
    else:
        i+=1
print(text)
#2
n = int(input('please enter a number 1<=n<=20 : '))
squares = []
a=1
while a<=n:
    squares.append(a**2)
    a+=1
print(squares)
#3
numbers = []
while 0<i<=10:
    numbers.append(i)
    i+=1
print(numbers)

numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)
num = []
for i in range(1,6):
    for j in range(1,i+1):
            print(j,end=' ')
    print()

i=1
total = 0
while i <=10:
    total +=i
    i+=1
print(total)


multiple = 2
for i in range(1,11):
    print(multiple*i)

i=0
kop = 2
while i<10:
    i+=1
    print(kop * i)


numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i>150 or i<=50:
        continue
    if i%5==0:
        print(i)

num = 75869
num = len(str(num))
num


num = 75869
count = 0
while num !=0:
    num = num//10
    count+=1
print(count)


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ') 
    print()


i=5
while i>=1:
    j=i
    while j>=1:
        print(j,end=' ')
        j -= 1
    print()
    i -= 1


list1 = [10, 20, 30, 40, 50]
n=len(list1)
while n>=1:
    print(list1[n-1])
    n-=1

for i in range(-10,0):
    print(i)

i=-10
while i<0:
    print(i)
    i+=1

for i in range(1,5):
    print(i)
print('Done!')

for i in range(25,51):
    is_prime = True
    for j in range(2,i):
        if i%j==0:
            is_prime = False
            break
    if is_prime == True and i> 1:
        print(i)  


a = 0
b = 1
while a <= 100:
    print(a)
    a, b = b, a + b

n = 10  # nechta son chiqishini xohlaysiz
a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b

n=1
while n<=5:
    k=1
    factorial = 1
    while k<=n:
        factorial = k*factorial
        k+=1
    n+=1
print(f'5! = {factorial}')   


list1 = [1, 10, 8, 6]
list2 = [8, 6, 10, 15]
list3 = []

for i in list1:
    if i not in list2:
        list3.append(i)

for j in list2:
    if j not in list1:
        list3.append(j)

print(list3)



