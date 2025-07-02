from datetime import date
employee_info = {
    'id':'102',
    'name':'Feruza',
    'department':'Foreign Economic Activities',
    'date_of_birth': 1994,
    'hired_date': date(2022,9,5)}
sorting_by_asc = dict(sorted(employee_info.items(), key=lambda item : str(item[1])))
sorting_by_desc = dict(sorted(employee_info.items(), key=lambda item : str(item[1]), reverse=True))
print(sorting_by_asc)
print(sorting_by_desc)
##
dict_numbers = {
    'bir' : 'one', 
    'ikki':'two', 
    'uch':'three', 
    'tort': 'four',
    'besh': 'five'
    }
sorting_asc = dict(sorted(dict_numbers.items(), key=lambda item: item[1]))
sorting_desc = dict(sorted(dict_numbers.items(), key=lambda item: item[1], reverse=True))
print(sorting_asc)
print(sorting_desc)
##
dict_numbers = {0:10, 1:20}
dict_numbers['2'] = '30'
dict_numbers
##
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
common_dicts = {**dic1,**dic2,**dic3}
common_dicts
##
n=int(input('please enter length of number: '))
square_dict = {}
for i in range(1,n+1):
    square_dict[i] = i*i
square_dict
##
import math
k = int(input('enter any number: '))
cube_dict = {}
for k in range(1,k+1):
    cube_dict[k] = int(math.pow(k,3))
cube_dict
##
l = int(input('please enter any number: '))
square_dict = {k:k*k for k in range(1,k+1)}
square_dict
##
set1 = {1,5,9,45}
set1
##
set2 = {'apple','banana','grape','limon','peach'}
for fruit in set2:
    print(fruit)
##
set2.add('pomigranate')
##
set2.remove('apple')
set2
##
if 'banana'in set2:
    set2.discard(fruit)
    print('updated set :',set2)
else:
    print('no change: ',set2)






































