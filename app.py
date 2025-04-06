import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
show_hist = st.checkbox('Mostrar histograma de odómetro')

if show_hist:
    st.write('Histograma de los valores del odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para diagrama de dispersión
show_scatter = st.checkbox('Mostrar diagrama de dispersión: odómetro vs precio')

if show_scatter:
    st.write('Diagrama de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price", color="type")
    st.plotly_chart(fig, use_container_width=True)

