import streamlit as st
import pandas as pd


@st.cache_data
def carregar_resultados():
    return pd.read_excel(
        "datasets/Resultado_Lotofacil.xlsx"
    )


@st.cache_data
def carregar_jogos():

    df = pd.read_excel(
        "datasets/Jogos_Realizados.xlsx"
    )

    colunas_dezenas = [
        col
        for col in df.columns
        if col.startswith("D")
    ]

    for col in colunas_dezenas:

        df[col] = df[col].astype("Int64")

    return df