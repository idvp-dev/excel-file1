import streamlit as st
import pandas as pd



#import pip
#pip.main(["install","openpyxl","plotly.express"])

import plotly.express as px

#st.title('Mi primera pagina web con Streamlit')

st.set_page_config(page_title='Reporte de Ventas',#nombre de la pagina
                   page_icon='moneybag:',#https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout='wide')

st.title(':clipboard: Reporte de Ventas') #titulo del dash
st.subheader('Compañía TECH SAS')
st.markdown('##') #para separar el título de los KPI's, se inserta un parrafo usando un campo de markdown

archivo_excel='/home/ivan/Documentos/UDEMY/STREAMLIT/VentasTienda.xlsx'
hoja_excel='Hoja 1'

#df = pd.read_excel('/home/ivan/Documentos/UDEMY/STREAMLIT/VentasTienda.xlsx')
#df = pd.read_excel('VentasTienda.xlsx')

df=pd.read_excel(archivo_excel,
                 sheet_name=hoja_excel,
                 usecols='A:I')

df['Precio'] = df['Precio'].astype(str).str.replace('$', '').str.replace(',', '').str.strip()
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')


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



#ventas_por_producto=(df_seleccion.groupby(by=['Producto']).sum()[['Precio']].sort_values(by='Precio'))


ventas_por_producto = (
    df_seleccion
    .groupby('Producto')['Precio']  # Especificamos la columna directamente
    .sum()
    .reset_index()  # Convertimos el índice en columna
    .sort_values('Precio', ascending=True)
)


fig_ventas_producto=px.bar(
ventas_por_producto,
x='Precio',
y=ventas_por_producto.index,
orientation='h',
title='<b> ventas por producto </b>',
color_discrete_sequence=['#f5b932']*len(ventas_por_producto),
template='plotly_white'

)

fig_ventas_producto.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=(dict(showgrid=False))
)



#ventas_por_vendedor=(df_seleccion.groupby(by=['Vendedor']).sum()[['Precio']].sort_values(by='Precio'))

ventas_por_vendedor = (
    df_seleccion
    .groupby('Vendedor')['Precio']  # Especificamos la columna directamente
    .sum()
    .reset_index()  # Convertimos el índice en columna
    .sort_values('Precio', ascending=True)
)




fig_ventas_vendedor=px.bar(
ventas_por_vendedor,
x='Precio',
y=ventas_por_vendedor.index,
#orientation='h',
title='<b> ventas por vendedor </b>',
color_discrete_sequence=['#f5b932']*len(ventas_por_vendedor),
template='plotly_white'

)

fig_ventas_vendedor.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
)

left_column, right_column=st.columns(2)
left_column.plotly_chart(fig_ventas_vendedor, use_container_width=True)
right_column.plotly_chart(fig_ventas_producto,use_container_width=True)


hide_st_style="""
              <style>
               footer {visibility : hidden;}
              </style>
              """

st.markdown(hide_st_style, unsafe_allow_html=True)






st.write(df)  