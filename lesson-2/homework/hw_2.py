from datetime import datetime
import random
import string
name=input("please, enter your mame:")
birth_year=int(input("please, enter your year of birth:"))
current_year=datetime.now().year
yosh=current_year-birth_year
print(f"Hello,{name}! Your are {yosh} yeras old.")
txt = 'LMaasleitbtui'
found1 = ''.join([txt[i] for i in range(0,len(txt),2)])
found2 = ''.join([txt[j] for j in range(1,len(txt),2)])
print(found1)
print(found2)
txt = 'MsaatmiazD'
found1 = ''.join([txt[i] for i in range(0,len(txt),2)])
found2 = ''.join([txt[j] for j in range(len(txt)-1,0,-2)])
print(found1)
print(found2)
txt = "I'am John. I am from London"
l=txt.index('L')
found1=''.join([txt[i] for i in range(l,len(txt),1) ])
print(found1)
soz = input("pleasecenter any word:")
teskari_soz = soz[::-1]
print(f"The reverse of this word is {teskari_soz}.")
soz = input("please enter any word:")
word_list = soz.split() 
vowel_count=0
vowels = ['a','o','u','i','e','A','O','U','I','E']
for word in word_list:
    for i in word:
        if i in vowels:
            vowel_count+=1
print(f"There are {vowel_count} vowels in {soz}")
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
numbers_list = [a,b,c]
maximal=max(numbers_list)
print(f"there are {numbers_list} list and max value is {maximal}.")
word = input('please enter any word: ')
i,j = 0,len(word)-1
is_palindrome = True
while i<j:
    if word[i] != word[j]:
        is_palindrome = False
        break
    i +=1
    j -=1
if is_palindrome:
    print('yes')
else:
    print('no')
  email = input('please enter any email address:')
if '@' in email:
    domain = email.split('@')[1]
    print(f'The domain of the {email} is: {domain}')
else:
    print(f'Invalid {email} address. Please include '@' symbol.')

length = int(input("Enter the desired password length: "))
letters = string.ascii_letters          # a-z, A-Z
digits = string.digits                  # 0-9
special_chars = string.punctuation      # !@#$%^&*()_+-=[]{}|;:,.<>?/
all_chars = letters + digits + special_chars
password = ''.join(random.choice(all_chars) for _ in range(length))
print(f"Your random password is: {password}")
