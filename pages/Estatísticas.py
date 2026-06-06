from pathlib import Path
import streamlit as st
import pandas as pd
from modules.loader import carregar_resultados

st.set_page_config(
    page_title="Estatísticas", # Nome da página no navegador
    #page_icon=str(icone), # ícone da página no navegador
    layout="wide" # tamanho/formato da página
)

df = carregar_resultados()

st.title("📊 Estatísticas") # título
st.divider() # Linha de separação entre seções