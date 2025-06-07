import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') 
st.write('Sprint 7')
hist_button = st.button('Construir graficos')  


if hist_button:  
 
    st.write('Sprint 7')

   
    fig = px.histogram(
        car_data,
        x="model_year",
        y="price",
        color="fuel",
        histfunc="sum"
    )
    st.plotly_chart(fig, use_container_width=True)


    scatter = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Relación entre año del modelo y precio"
    )
    st.plotly_chart(scatter, use_container_width=True)
