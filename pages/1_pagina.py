import streamlit as st

def pagina():
    st.write("Prueba")

st.set_page_config(page_title="Página 1",page_icon="📈")
st.markdown("# Página 1")
st.sidebar.header("Filtros")
st.write("Hola esto es una prueba")

pagina()
