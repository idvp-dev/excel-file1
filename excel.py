import streamlit as st
import pandas as pd
import plotly.express as px


import pip
pip.main(["install","openpyxl","plotly-express"])

#st.title('Mi primera pagina web con Streamlit')

st.set_page_config(page_title='Reporte de Ventas',#nombre de la pagina
                   page_icon='moneybag:',#https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout='wide')

st.title(':clipboard: Reporte de Ventas') #titulo del dash
st.subheader('Compañía TECH SAS')
st.markdown('##') #para separar el título de los KPI's, se inserta un parrafo usando un campo de markdown

archivo_excel='VentasTienda.xlsx'
hoja_excel='Hoja 1'

#df = pd.read_excel('/home/ivan/Documentos/UDEMY/STREAMLIT/VentasTienda.xlsx')
#df = pd.read_excel('VentasTienda.xlsx')

df=pd.read_excel(archivo_excel,
                 sheet_name=hoja_excel,
                 usecols='A:I')


st.sidebar.header('Filtros:') #barra lateral para filtros

vendedor=st.sidebar.multiselect(
      'Seleccione el vendedor:',
      options=df['Vendedor'].unique(),
      default=df['Vendedor'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)

categoría=st.sidebar.multiselect(
      'Seleccione el vendedor:',
      options=df['Categoría'].unique(),
      default=df['Categoría'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)

provinia=st.sidebar.multiselect(
      'Seleccione el vendedor:',
      options=df['Provincia'].unique(),
      default=df['Provincia'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)

st.write(df)  