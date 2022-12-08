'''
Reto Modulo 5 Tec de Monterrey
Héctor Gabriel Sánchez Pérez
'''
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_page_config(page_title="Reto Modulo 5", layout="wide")

@st.cache
def full_df():
    data = pd.read_csv('Employees.csv')
    return data

@st.cache
def filtered_df(nrows):
    data = full_df().head(nrows)
    return data

@st.cache
def filtered_employees(employee_ID, hometown, unit, education):
    data = filtered_df(renglones).loc[
        (filtered_df(renglones)["Employee_ID"].str.upper().str.contains(employee_ID.upper()))&
        (filtered_df(renglones)["Hometown"].str.upper().str.contains(hometown.upper()))&
        (filtered_df(renglones)["Unit"].str.upper().str.contains(unit.upper()))&
        (filtered_df(renglones)["Education_Level"]==education)
        ]
    return data

#SIDEBAR
with st.sidebar:
    st.image('https://cdn.datavoro.com/datavorocontainer/2022/09/IMG_1787-667x1024.jpg', width=100, caption="Hector Sanchez")

    mostrar = st.checkbox("Mostrar Dataframe")
    renglones = st.slider("Seleccionar el número de renglones a analizar:", min_value=1, max_value=int(full_df()["Employee_ID"].count()), step=99, value=500)
    
    st.subheader("Buscador de Empleados")
    employee_ID = st.text_input("Employee_ID")
    hometown = st.selectbox("Ciudad", filtered_df(renglones)["Hometown"].unique())
    unit = st.selectbox("Unidad Funcional", filtered_df(renglones)["Unit"].unique())
    educacion = st.selectbox("Nivel Educativo", filtered_df(renglones)["Education_Level"].unique())

    filter_button = st.button("Filtrar")

    renglones_filtrados = int(filtered_employees(employee_ID, hometown, unit, educacion)["Employee_ID"].count())

# MAIN SECTION
st.title("Reto")
st.header("Modulo 5")
st.markdown("### Aplicación en Streamlit para el Reto del Modulo 5")
st.markdown("---")

if mostrar == True:

    if filter_button == True:

        st.subheader("Esta es la tabla con los filtros aplicados del Buscador de Empleados")
        st.caption(f"Empleados encontrados: {renglones_filtrados} de un total de {renglones} empleados analizados")
        filtered = filtered_employees(employee_ID, hometown, unit, educacion)
        filtered2 = filtered_df(renglones)
        st.dataframe(filtered)

        st.markdown('---')
        st.subheader("Histograma de la tabla filtrada")
        fig = px.histogram(data_frame=filtered, x='Age')
        st.plotly_chart(fig)

        st.markdown('---')
        st.subheader("Gráfica de Frecuencias de la tabla filtrada")
        subtable = filtered.groupby("Unit").count()
        fig = px.bar(data_frame=subtable, y='Employee_ID', color="Employee_ID")
        st.plotly_chart(fig)

        st.markdown('---')
        st.subheader(f"Indice de Deserción por Ciudad de la tabla filtrada: {renglones_filtrados} empleados")
        subtable2 = filtered.loc[:,["Hometown", "Attrition_rate"]].groupby("Hometown").mean().sort_values(by="Attrition_rate", ascending=False)
        fig = px.bar(data_frame=subtable2, y='Attrition_rate', color="Attrition_rate")
        st.plotly_chart(fig)

        st.markdown('---')
        st.subheader(f"Indice de Deserción por Ciudad de las renglones analizados: {renglones} analizados")
        subtable2 = filtered2.loc[:,["Hometown", "Attrition_rate"]].groupby("Hometown").mean().sort_values(by="Attrition_rate", ascending=False)
        fig = px.bar(data_frame=subtable2, y='Attrition_rate', color="Attrition_rate")
        st.plotly_chart(fig)

        st.markdown('---')
        st.subheader("Indice de Deserción por Edad de la tabla filtrada")
        subtable2 = filtered.loc[:,["Age", "Attrition_rate"]].groupby("Age").mean().sort_values(by="Attrition_rate", ascending=False)
        fig = px.bar(data_frame=subtable2, y='Attrition_rate', color="Attrition_rate")
        st.plotly_chart(fig)    

        st.markdown('---')
        st.subheader("Relación entre tiempo de servicio y tasa de deserción de los renglones filtrados")
        subtable3 = filtered.loc[:,["Time_of_service", "Attrition_rate"]]
        fig = px.scatter(data_frame=subtable3, x='Time_of_service', y='Attrition_rate')
        st.plotly_chart(fig)

        st.markdown('---')

