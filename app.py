import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Data viewer')

car_data = pd.read_csv(
    'vehicles_us.csv')  # leer los datos



data_button = st.checkbox('Mostrar Datos')  # crear botón de data
mostrar_sin_nulos = st.checkbox('Mostrar solo datos sin valores nulos')

if data_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Visualización de los datos')
    
    if mostrar_sin_nulos:
        car_data_a_mostrar = car_data.dropna()
    else:
        car_data_a_mostrar = car_data
    
    st.dataframe(car_data_a_mostrar)


hist_button = st.button('Construir histograma')  # crear un botón


if hist_button:
    # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir grafico de dispersión')


if disp_button:
    # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)


