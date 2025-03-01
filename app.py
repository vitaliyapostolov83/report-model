import streamlit as st
import pandas as pd
import requests
from io import StringIO
import seaborn as sns
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

    # Створення графіка
    fig, ax = plt.subplots(figsize=(10, 6))  # Розмір графіка
    sns.scatterplot(x=data['column_name_1'], y=data['column_name_2'], ax=ax)  # Замість 'column_name_1' і 'column_name_2' поставте ваші колонки

    # Додавання назв осей
    ax.set_xlabel('Назва осі X')
    ax.set_ylabel('Назва осі Y')
    ax.set_title('Графік залежності')

    # Виведення графіка
    st.pyplot(fig)
    
else:
    st.write("Не вдалося завантажити файл.")
