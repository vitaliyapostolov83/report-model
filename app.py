import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.title("Модель звіту по меблевику")# Заголовок
number = st.slider("Виберіть кількість рядків таблиці", 1, 1000)# Додавання слайдера
st.write(f"Ви вибрали кількість рядків: {number}")
url = "https://raw.githubusercontent.com/vitaliyapostolov83/report-model/main/flats.csv" # URL до файлу на GitHub (візьми Raw файл)
response = requests.get(url) # Завантажуємо файл

if response.status_code == 200:# Якщо файл був успішно завантажений
    data = pd.read_csv(StringIO(response.text))# Завантажуємо CSV в Pandas DataFrame
    data = data.head(number)# Обмежуємо кількість рядків відповідно до вибору на слайдері
    st.write(data)# Вивести обмежену таблицю на сторінці Streamlit
else:
    st.write("Не вдалося завантажити файл.")
