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
      'Seleccione la categoría:',
      options=df['Categoría'].unique(),
      default=df['Categoría'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)

provincia=st.sidebar.multiselect(
      'Seleccione la provincia:',
      options=df['Provincia'].unique(),
      default=df['Provincia'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)


producto=st.sidebar.multiselect(
      'Seleccione el producto:',
      options=df['Producto'].unique(),
      default=df['Producto'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)

forma_pago=st.sidebar.multiselect(
      'Seleccione la forma de pago:',
      options=df['Forma de pago'].unique(),
      default=df['Forma de pago'].unique() #esto para dejar un filtro en específico pero vamos a dejarlos por default

)

df_seleccion=df.query('Vendedor==@vendedor & Categoría==@categoría & Producto==@producto')


total_ventas=int(df_seleccion['Precio'].sum())

total_facturas=int(df_seleccion['Precio'].count())

left_column, right_column=st.columns(2)

with left_column:
    st.subheader('Ventas totales: ')
    st.subheader(f'US $ {total_ventas:,}')

with right_column:
    st.subheader('Facturas: ')
    st.subheader(f' {total_facturas}')

st.markdown('---')

st.dataframe(df_seleccion)

