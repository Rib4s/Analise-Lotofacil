from pathlib import Path
import streamlit as st
import pandas as pd

#st.write('https://docs.streamlit.io')

pasta_datasets = (Path(__file__).parent.parent / "datasets").resolve()
arquivo_resultados = pasta_datasets / "Resultado_Lotofacil.xlsx"

tabela = pd.read_excel(arquivo_resultados)
st.dataframe(tabela)
