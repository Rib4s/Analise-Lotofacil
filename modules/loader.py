from pathlib import Path
from datetime import datetime

import pandas as pd
import streamlit as st


@st.cache_data
def _carregar_excel_cache(
    arquivo,
    ultima_modificacao
):
    return pd.read_excel(arquivo)


def carregar_resultados():

    arquivo = Path(
        "datasets/Resultado_Lotofacil.xlsx"
    )

    return _carregar_excel_cache(
        str(arquivo),
        arquivo.stat().st_mtime
    )


def carregar_jogos():

    arquivo = Path(
        "datasets/Jogos_Realizados.xlsx"
    )

    return _carregar_excel_cache(
        str(arquivo),
        arquivo.stat().st_mtime
    )


def obter_data_atualizacao_resultados():

    arquivo = Path(
        "datasets/Resultado_Lotofacil.xlsx"
    )

    return datetime.fromtimestamp(
        arquivo.stat().st_mtime
    )


def obter_data_atualizacao_jogos():

    arquivo = Path(
        "datasets/Jogos_Realizados.xlsx"
    )

    return datetime.fromtimestamp(
        arquivo.stat().st_mtime
    )