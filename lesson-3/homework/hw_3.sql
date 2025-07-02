birinchi = input('please enter different fruits:')
ikkinchi = input('please enter different fruits:')
uchinchi = input('please enter different fruits:')
tortinchi = input('please enter different fruits:')
beshinchi = input('please enter different fruits:')
fruits = [birinchi,ikkinchi,uchinchi,tortinchi,beshinchi]
print(fruits[4])

mevalar_input = input("5 xil mevani, vergul bilan ajratib kiriting: ")
fruits = mevalar_input.split(',')

print("Uchinchi meva:",fruits, fruits[2])
##
gap = input('gap kiriting:')
almashtirmoqchi = input('qaysi sozni almashtirmoqchisiz, kiriting u sozni:')
qaysi_sozga = input('qanday sozga almashtirmoqchisiz, kiriting:')
replaced_soz = gap.replace(almashtirmoqchi,qaysi_sozga)
print(f"sizning \n{gap} \n gapingiz quyidagicha ozgardi\n{replaced_soz}")
##
numbers = [1,5,88,-78,95,0,4,-23]
new_list = []
first_num = numbers[0]
middle_num = numbers[(len(numbers)-1)//2]
last_num = numbers[-1]
new_list = [first_num,middle_num,last_num]
print(new_list)
##
movies = ['titanic','brothers','smith','london']
tuple_movies = tuple(movies)
print(movies)
print(tuple_movies)
##
cities = ['london','parij','tokiyo','washington','ottawa','seoul']
city = input('please enter the city you are searching for: ')
if city in cities:
    print(f"siz izlagan shahar ro'yxatda mavjud")
else:
    print("Bunday shahar mavjud emas")
##
books_list = ['history','japan','being wise','datascience','python']
new_books_list1 = books_list*2
new_books_list2 = [*books_list,*books_list]
print(new_books_list1)
print(new_books_list2)
##
any_list = ['apple','pen','trees','road','cars','flowers']
print(any_list)
any_list[0],any_list[-1]=any_list[-1],any_list[0]
print(any_list)
##
list_of_tuple = (-75,0,15,33,-21,45,1145,-4,19,23)
new_list_of_tuple = list_of_tuple[3:7]
new_list_of_tuple
##
list_of_colours = ['red','blue','red', 'orange','yellow','orange','blue','pink','green','blue']
color = input('please enter any color you like:')
counting_color = list_of_colours.count(color)
counting_color
##
tuple_of_animals = ['rabbit','sheep','lion','duck','dog','hors']
animal = input('please enter any animal you like:')
index = tuple_of_animals.index(animal)
print(index)
##
tuple1 = [1,5,9,7,8,3,5]
tuple2 = [-1,-8,9,-55,-78]
common = tuple1+tuple2
common
##
list = [1,5,8,55,44,7,8,3]
tuple = (1,8,5,4,8,-77,99,7,102)
print("length of the list =",len(list))
print("length of the tuple =",len(tuple))
##
tuple_data = (0,20,36,44,89,71,235)
newtuple =list(tuple_data)
print(newtuple)
##
tuple= (0,20,36,44,89,71,235)
lst=list(tuple)
print(lst)
##
tuple= (0,20,36,44,89,71,235)

maximum_element = max(tuple)
minimum_element = min(tuple)
print(f"maximum = {maximum_element} and minimum = {minimum_element}")
##
tuple = ('ali','shokir','salim','non','suv')
reversed_tuple = tuple[::-1]
reversed_tuple
books = ['math','biology','science']
fruits = ['apple','granate','peach']
new = books+fruits
print(new)
my_tuple = 12,'john'
print(type(my_tuple))
print(my_tuple)
my_data = [(1,'john',28,'london'),(2,'susan',30,'los angeles'),(3,'ali',35,'uzb')]
print(my_data)
my_tuple = (2,'sojida', 24, 'london')
print(my_tuple.count('sojida'))
print(my_tuple.index('london'))
print(my_tuple[2:10])
































































































