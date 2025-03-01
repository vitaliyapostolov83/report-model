import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.title("Модель звіту по меблевику")# Заголовок
number = st.slider("Виберіть кількість рядків таблиці", 1, 1000)# Додавання слайдера
st.write(f"Ви вибрали кількість рядків: {number}")
url = "https://raw.githubusercontent.com/vitaliyapostolov83/report-model/main/flats.csv" # URL до файлу на GitHub (візьми Raw файл)
response = requests.get(url) # Завантажуємо файл

# Якщо файл був успішно завантажений
if response.status_code == 200:
    # Завантажуємо CSV в Pandas DataFrame
    data = pd.read_csv(StringIO(response.text))
    
    # Обмежуємо кількість рядків відповідно до вибору на слайдері
    data = data.head(number)
    
    # Вивести таблицю з налаштуванням ширини колонок
    st.dataframe(data, width=700)  # Регулює ширину всієї таблиці (у пікселях)
    
else:
    st.write("Не вдалося завантажити файл.")
