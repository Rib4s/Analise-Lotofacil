from pathlib import Path
import streamlit as st
import pandas as pd
from modules.loader import carregar_resultados

st.set_page_config(
    page_title="Resultados", # Nome da página no navegador
    #page_icon=str(icone), # ícone da página no navegador
    layout="wide" # tamanho/formato da página
)

df = carregar_resultados()

st.title("📋 Resultados") # título
st.divider() # Linha de separação entre seções

col1, col2, col3 = st.columns(3, gap="large")

with col1:
        concurso = st.selectbox(
        "Selecione um concurso",
        options=df["Concurso"].sort_values(ascending=False)
    )
resultado = df[df["Concurso"] == concurso]

with col2:
    dezenas = []

    for i in range(1, 16):
        dezenas.append(resultado[f"Bola{i}"].iloc[0])

    st.write("### Dezenas sorteadas")

    st.write(" | ".join(f"{n:02d}" for n in dezenas))

with col3:
    st.metric("Total de Concursos", len(df))


st.divider() # Linha de separação entre seções

st.dataframe(
    df.set_index("Concurso"),
    use_container_width=True
)


# pasta_datasets = (Path(__file__).parent.parent / "datasets").resolve()
# arquivo_resultados = pasta_datasets / "Resultado_Lotofacil.xlsx"

# tabela = pd.read_excel(arquivo_resultados)
# st.dataframe(tabela)
