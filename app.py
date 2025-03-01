import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Заголовок
st.title("Модель звіту по меблевику")

# Додавання слайдера
number = st.slider("Виберіть кількість рядків таблиці", 1, 1000)
st.write(f"Ви вибрали кількість рядків: {number}")

# URL до файлу на GitHub (візьми Raw файл)
url = "https://raw.githubusercontent.com/vitaliyapostolov83/report-model/main/flats.csv"  # Замінено на правильний шлях до твого файлу

# Завантажуємо файл
response = requests.get(url)

# Якщо файл був успішно завантажений
if response.status_code == 200:
    # Завантажуємо CSV в Pandas DataFrame
    data = pd.read_csv(StringIO(response.text))
    
    # Обмежуємо кількість рядків відповідно до вибору на слайдері
    data = data.head(number)
    
    # Вивести обмежену таблицю на сторінці Streamlit
    st.write(data)
else:
    st.write("Не вдалося завантажити файл.")
