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


hist_button = st.checkbox('Construir histograma')  # crear un botón


if hist_button:
    # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.checkbox('Construir grafico de dispersión')


if disp_button:
    # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)


grupo_seleccionado1 = st.selectbox('Seleccione tipo 1', car_data['type'].unique())
grupo_seleccionado2 = st.selectbox('Seleccione tipo 2', car_data['type'].unique())

df_filtrado1 = car_data[car_data['type'] == grupo_seleccionado1]
df_filtrado1['grupo'] = grupo_seleccionado1

df_filtrado2 = car_data[car_data['type'] == grupo_seleccionado2]
df_filtrado2['grupo'] = grupo_seleccionado2

df_combinado = pd.concat([df_filtrado1, df_filtrado2])

fig3 = px.histogram(df_combinado, x='price', color='grupo', barmode='overlay', nbins=50, title=f'Histograma de precios para {grupo_seleccionado1} y {grupo_seleccionado2}')

st.plotly_chart(fig3, use_container_width=True)


fig4 = px.bar(car_data, x='model')
st.plotly_chart(fig4)