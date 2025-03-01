import streamlit as st
import pandas as pd
import numpy as np

# Заголовок
st.title("Модель звіту по меблевику")

# Додавання слайдера
number = st.slider("Виберіть кількість рядків таблиці", 1, 1000)
st.write(f"Ви вибрали кількість строк {number}")

# Створення таблиці з Pandas
data = pd.DataFrame({
    'Число': np.arange(1, number+1),
    'Квадрат': np.arange(1, number+1) ** 2
})

# Виведення таблиці
st.write(data)
