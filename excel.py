import streamlit as st
import pandas as pd

import pip
pip.main(["install","openpyxl"])

st.title('Mi primera pagina web con Streamlit')

#df = pd.read_excel('/home/ivan/Documentos/UDEMY/STREAMLIT/VentasTienda.xlsx')
df = pd.read_excel('VentasTienda.xlsx')

st.write(df)  