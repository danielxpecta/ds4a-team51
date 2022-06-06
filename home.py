import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Team51",
        page_icon="🏠"
    )

    st.write("# Prueba")
    
