import streamlit as st
import pandas as pd
import os

def pagina():
    st.write("Prueba")

df = pd.read_excel(os.path.join("data","BD.xlsx"), header=1)


st.set_page_config(page_title="Página 1",page_icon="📈")
st.markdown("# Página 1")

#----------------------------------
# CREATING FLTERS FOR THE SIDEBAR:s
#1. Location filter
#2. Year Filter
#----------------------------------
container_location= st.sidebar.container() #Creates a container for locations filter in the sidebar
all_locations = container_location.checkbox("Seleccionar todo",key="check_locations") #Creates a checkbox for the user wants to see some locations or all of them

if all_locations:
    location= container_location.multiselect(
        "Elija una/varias localidad(es)", list(df["LOCALIDAD"].drop_duplicates().dropna()),list(df["LOCALIDAD"].drop_duplicates().dropna())
        ) #If all locations are checked the multiselector show all locations 
else:
    location= container_location.multiselect(
        "Elija una/varias localidad(es)", list(df["LOCALIDAD"].drop_duplicates().dropna()),"SUBA"
        )#If all locations is not checked the multiselector only SUBA by default
        

container_year= st.sidebar.container() #Creates a container for years filter in the sidebar
all_years = container_year.checkbox("Seleccionar todo",key="check_years") #Creates a checkbox for the user wants to see some years or all of them
if all_years:
    year= container_year.multiselect(
        "Elija una/varios año(s)", list(df["AÑO"].drop_duplicates().dropna()),list(df["AÑO"].drop_duplicates().dropna())
        ) #If all years are checked the multiselector show all years 
else:
    year= container_year.multiselect(
        "Elija una/varios año(s)", list(df["AÑO"].drop_duplicates().dropna()),2019
        ) #If all years is not checked the multiselector show 2019 by default


#----------------------------------
# CREATING PLOTS FOR THE SIDEBAR:
#1. Location filter
#2. Year Filter
#----------------------------------

st.write("Porcentaje de cumplimiento por localidad")

pagina()
