from pathlib import Path
import streamlit as st

icone = Path("datasets/Favicon JKel.png")  

st.set_page_config(
    page_title="Análise Lotofácil", # Nome da página no navegador
    page_icon=str(icone), # ícone da página no navegador
    layout="wide" # tamanho/formato da página
)

st.title("📊 Projeto Lotofácil") # título
st.write("Olá, Paulo! 🚀") # descrição abaixo do título
st.divider() # Linha de separação entre seções
st.markdown( # texto estilizado com partes em cores diferentes
    """
<span style="color: green;"><b>• pandas</b></span> : para manipulação de dados em tabelas  
<span style="color: green;"><b>• plotly</b></span> : para geração de gráficos  
<span style="color: green;"><b>• streamlit</b></span> : para criação desse webapp interativo
""",
    unsafe_allow_html=True
)