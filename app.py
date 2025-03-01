import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Завантаження даних (наприклад, CSV файл)
url = "https://raw.githubusercontent.com/vitaliyapostolov83/report-model/main/flats.csv"
response = requests.get(url)

if response.status_code == 200:
    data = pd.read_csv(StringIO(response.text))
    st.write(data)  # Показуємо таблицю

    # Візуалізація графіка
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['column_name'], kde=True)  # Приклад з гістограмою для стовпця
    st.pyplot()  # Виводимо графік
else:
    st.write("Не вдалося завантажити файл.")
