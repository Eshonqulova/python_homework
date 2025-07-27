import json
with open("students.json",'r',encoding='utf-8') as f:
    data = json.load(f)
    
for student in data['students']:
    print(f"{student['id']}, {student['name']} , {student['age']} years old.")


import requests
url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToLzEHFymfSgkKLuOn1XIcqtrGxg7_ObjRnA&s'
res = requests.get(url)
print(res.text) # text beradi
print(res.status_code) # kod beradi 200, 404 kabi

with open ('my_new_image2.png','wb') as f:
    f.write(res.content)


import requests
units = 'metric'
API_key = 'f8cc46d50a674109995121357251402'
city_names = ['Tashkent','Bukhara','Surkhandaryo', 'Samarkand']
for city in city_names:
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units={units}'
    resp = requests.get(url)
    my_data = resp.json()
    print(resp.text)

#city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.
city = 'Tashkent'
key = 'f8cc46d50a674109995121357251402'
url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no'
response = requests.get(url)
data = response.json()


city = data['location']['name']
temp = data['current']['temp_c']
humidity = data['current']['humidity']
print(f'city {city} humidity:{humidity}, temperature is {temp}°C')

book_id = input("books' id: ")
book_name = input("books' name: ")
author_name = input("books' author name: ")     
news = {"book_id": book_id, "name": book_name, "author_name": author_name}

with open('library.json','r') as f:
    my_data = json.load(f)

for i in my_data.values():
    i.append(news)

with open('library.json', 'w') as f:
    my_data = json.dump(my_data,f, indent=2)

import requests
import random
API_key = '75362e84'
filmlar = {
    "action" : ["john Wick", "Mad Max: Fury Road", "Gladiator"],
    "comedy" : ["The mask", "Home alone", "Smmiths family"],
    "drama" : ["Forrest Gump", "The Shawshank Redemption", "The Pursuit of Happyness"],
    "sci-fi" : ["Inception", "The Matrix", "Avatar"],
    "horror" : ["The Conjuring", "Get Out", "It"]
}
janr = input("Janrni kiriting(action, comedy, drama, sci-fi,horror): ")

if janr in filmlar:
    film_nomi = random.choice(filmlar[janr])
    url = f" http://www.omdbapi.com/?i=tt3896198&apikey=75362e84"
    javob = requests.get(url)
    data = javob.json()
    new_data = json.dumps(data,indent=2)
    print(new_data)
    
    if data["Response"] == "True":
        print("\n🎬 Nomi:", data["Title"])
        print("📅 Yili:", data["Year"])
        print("⭐ IMDB bahosi:", data["imdbRating"])
        print("📖 Qisqacha mazmuni:", data["Plot"])
    else:
        print("Film topilmadi:", data["Error"])

else:
    print("kechirasiz bu janr mavjud emas.")

