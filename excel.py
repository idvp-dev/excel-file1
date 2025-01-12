import streamlit as st
import pandas as pd

st.title('Mi primera pagina web con Streamlit')

df=pd.read_excel('VentasTienda.xlsx')

st.write(df)