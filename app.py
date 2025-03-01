import streamlit as st
import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

# Заголовок
st.title("Модель звіту по меблевику")

# Додавання слайдера
number = st.slider("Виберіть кількість рядків таблиці", 1, 1000)
st.write(f"Ви вибрали кількість рядків: {number}")

# URL до файлу на GitHub (візьми Raw файл)
url = "https://raw.githubusercontent.com/vitaliyapostolov83/report-model/main/flats.csv"

# Завантажуємо файл
response = requests.get(url)

# Якщо файл був успішно завантажений
if response.status_code == 200:
    # Завантажуємо CSV в Pandas DataFrame
    data = pd.read_csv(StringIO(response.text))
    
    # Обмежуємо кількість рядків відповідно до вибору на слайдері
    data = data.head(number)
    
    # Вивести таблицю з налаштуванням ширини колонок
    st.dataframe(data, width=700)  # Регулює ширину всієї таблиці (у пікселях)
    
    # Створення графіка (наприклад, гістограма для одного з стовпців)
    st.subheader('Графік розподілу даних')
    plt.figure(figsize=(10, 6))  # Налаштування розміру графіка
    
    # Використання matplotlib для побудови графіка, наприклад, гістограма для одного стовпця
    if 'Ціна' in data.columns:  # Перевірка, чи існує стовпець з ім'ям 'column_name'
        plt.hist(data['Ціна'], bins=30, edgecolor='black')
        plt.title('Гістограма для стовпця Ціна')
        plt.xlabel('Значення')
        plt.ylabel('Частота')
        st.pyplot()  # Вивести графік в Streamlit
    else:
        st.write("Стовпець 'Ціна' не знайдений у даних.")
else:
    st.write("Не вдалося завантажити файл.")
