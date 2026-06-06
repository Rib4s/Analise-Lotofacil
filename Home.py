from pathlib import Path
import streamlit as st

icone = Path("datasets/Favicon JKel.png")  

st.set_page_config(
    page_title="Análise Lotofácil", # Nome da página no navegador
    page_icon=str(icone), # ícone da página no navegador
    layout="wide" # tamanho/formato da página
)

st.title("🏠 Projeto Lotofácil") # título
st.divider() # Linha de separação entre seções
st.write("""Bem-vindo ao painel de análise da Lotofácil.\n
Utilize o menu lateral para acessar:""") # descrição abaixo do título
st.markdown( # texto estilizado com partes em cores diferentes
    """
<span style="color: green;"><b>• Resultados</b></span> : para visualização dos resultados dos concursos\n 
<span style="color: green;"><b>• Estatísticas</b></span> : para análise estatística dos resultados dos concursos\n 
<span style="color: green;"><b>• Gerador de Jogos</b></span> : para geração de jogos com base em critérios estatísticos\n
<span style="color: green;"><b>• Análise Avançada</b></span> : para análise avançada utilizando técnicas de machine learning e inteligência artificial\n
""",
    unsafe_allow_html=True
)