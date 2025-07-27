from datetime import date, datetime, time, timedelta
from dateutil.relativedelta import relativedelta

formats = ["%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d", "%d.%m.%Y","%Y.%m.%d"]
birth_input = input("Enter your birthdate (in any common format): ")
birth_date = None
for fmt in formats:
    try:
        birth_date = datetime.strptime(birth_input, fmt).date()
        break
    except:
        continue

if birth_date:
    today_date = date.today()
    age = relativedelta(today_date, birth_date)
    print(age.years, "yil", age.months, "oy", age.days, "kun")
else:
    print("Notog‘ri sana formati.")

birth_input = input("enter your birth date(YYYY-MM-DD): ")
try:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today_date = date.today()
    next_birthday = birth_date.replace(year=today_date.year)
    if next_birthday< today_date:
        next_birthday = next_birthday.replace(year=today_date.year + 1)
    difference_days = abs(next_birthday - today_date).days
    print(f"{difference_days} kun qoldi sizning tug'ulgan kuningizgacha")
except ValueError:
    print("to'g'ri formatni kiriting!")    

import math 
current_input = input("enter current date and time (e.g. 2025-07-18 13:30): ")
hours = int(input("Enter meeting duration (hours): "))
minutes = int(input("Enter meeting duration (minutes): "))
try:
    current_datetime = datetime.strptime(current_input, "%Y-%m-%d %H:%M")
    duration = timedelta(hours=hours, minutes=minutes)
    ending_datetime = current_datetime + duration
    print("🕒 Meeting will end at:", ending_datetime.strftime("%Y-%m-%d %H:%M"))
except ValueError:
    print("Invalid date/time format. Please use YYYY-MM-DD HH:MM")

import pytz
main_timezones = [
    "Asia/Tashkent", "UTC", "US/Eastern", "Europe/London",
    "Asia/Dubai", "Asia/Kolkata", "Asia/Seoul", "Asia/Tokyo", "Europe/Moscow"
]
print("Quyidagi timezone-lardan birini tanlang:")
for tz in main_timezones:
    print("-", tz)

date_input = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_zone = input("Enter your current timezone: ")
to_zone = input("Enter the timezone you want to convert to: ")
try:
    naive_datetime = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
    from_timezone = pytz.timezone(from_zone)
    to_timezone = pytz.timezone(to_zone)
    localized_datetime = from_timezone.localize(naive_datetime)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    print("Converted date and time in", to_zone, "→", converted_datetime.strftime("%Y-%m-%d %H:%M"))
except Exception as e:
    print("⚠️ Xatolik:", e)
    print("Iltimos, formatni va timezone nomlarini to'g'ri kiriting.")


from datetime import datetime
import time
future_time_str = input("Kelajakdagi sanani kiriting (YYYY-MM-DD HH:MM:SS): ")
try:
    future_time = datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        remaining_time = future_time - now
        if remaining_time.total_seconds() <= 0:
            print("⏰ Vaqt tugadi!")
            break
        print("Qolgan vaqt:", remaining_time)
        # Har 1 soniyada yangilab turadi
        time.sleep(60)
except ValueError:
    print("Iltimos, sanani to'g'ri formatda kiriting: YYYY-MM-DD HH:MM:SS")


email_input = input("please enter your new email: ")
try:
    parts = email_input.split('@')
    if len(parts) !=2 or not parts[0] or not parts[1] or '.' not in parts[1]:
        raise ValueError("Email format xato")
    print("Email to'g'ri ko'rinishda kiritildi: ", email_input)

except Exception as e:
    print("Xatolik:",e)


num_input = input("enter tel num: ")
try:
    digits = ''.join([c for c in num_input if c.isdigit()])
    if len(digits) != 10:
        raise ValueError("Phone number must be exactly 10 digits.")
    formatted = f"your number is ({digits[0:3]}) {digits[3:6]} - {digits[6:10]}"
    print("Formatted phone number:", formatted)
except Exception as e:
    print('Xatolik:',e)

import re
def check_password_strength(password):
    if (
        len(password)>=8 
        and re.search(r"[A-Z]",password) 
        and re.search(r"[a-z]",password) 
        and re.search(r"[0-9]",password)
        and re.search(r"\W",password)
    ):
        return "Strong password"
    else:
        return "Weak password! It must be at least 8 characters and include uppercase, lowercase, and digits."

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)


import re
def checking_password(login):
    if len(login)<8:
        return "Password too short! Must be at least 8 characters."
    if not re.search(r"[A-Z]",login):
        return "password contains at list one uppercase letter."
    if not re.search(r"[a-z]",login):
        return "password contains at list one lowercase letter."
    if not re.search(r"\d",login):
        return "pasword must contain at list one digit."
    if not re.search(r"\W",login):
        return "pasword must contain at list one special character (e.g., !@#$%)."
    return "Strong password!"

if __name__ == "__main__":
    user_login = input("enter your password: ")
    result = checking_password(user_login)
    print(result)

import re

def checking_password(login):
    if len(login) < 8:
        return "❌ Password too short! Must be at least 8 characters."
    if not re.search(r"[A-Z]", login):
        return "❌ Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", login):
        return "❌ Password must contain at least one lowercase letter."
    if not re.search(r"\d", login):  # to‘g‘rilangan
        return "❌ Password must contain at least one digit."
    if not re.search(r"\W", login):  # to‘g‘rilangan
        return "❌ Password must contain at least one special character (e.g., !@#$%)."
    return "✅ Strong password!"

if __name__ == "__main__":
    user_login = input("Enter your password: ")
    result = checking_password(user_login)
    print(result)

import re  # re modulini import qilish kerak

def word_finder(text, word):
    pattern = r"\b" + re.escape(word) + r"\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return matches  # bu yerda recursive chaqiruv emas, 'matches' ni qaytarish kerak

if __name__ == "__main__":
    sample_text = """
    Python is a powerful programming language. python can be used for data analysis,
    web development, and automation. Many developers enjoy coding in Python.
    """
    search_word = input("Enter the word to search: ")
    results = word_finder(sample_text, search_word)  # funksiya nomi to'g'ri bo'lishi kerak

    print(f"Found '{search_word}' {len(results)} times.")
    for i, word in enumerate(results, 1):
        print(f"{i}. {word}")



