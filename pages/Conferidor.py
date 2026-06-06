import streamlit as st

from modules.loader import (
    carregar_jogos,
    carregar_resultados,
    obter_data_atualizacao_jogos,
    obter_data_atualizacao_resultados
)
from modules.conferidor import conferir_intervalo


def destacar_premiacao(valor, cor):
    if valor > 0:
        return (
            f"color: {cor}; "
            "font-weight: bold; "
            "text-align: center;"
        )
    return "text-align: center;"

def destacar_resultado_liquido(valor):

    if valor > 0:
        return (
            "color: #22c55e;"
            "font-weight: bold;"
        )

    if valor < 0:
        return (
            "color: #ef4444;"
            "font-weight: bold;"
        )

    return ""

def formatar_moeda_br(valor):

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

st.set_page_config(
    page_title="Conferidor",
    layout="wide"
)

# Carregamento dos dados
df_jogos = carregar_jogos()
df_resultados = carregar_resultados()
data_jogos = obter_data_atualizacao_jogos()

data_resultados = (
    obter_data_atualizacao_resultados()
)

# Título
st.title("✅ Conferidor de Jogos")

col_data1, col_data2 = st.columns(2)

with col_data1:

    st.caption(
        "📅 Jogos atualizados em: "
        + data_jogos.strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    )

with col_data2:

    st.caption(
        "🎲 Resultados atualizados em: "
        + data_resultados.strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    )

st.divider()

# # Métricas iniciais
# col11, col12 = st.columns(2)

# with col11:
#     st.metric("Jogos Cadastrados", len(df_jogos))

# with col12:
#     st.metric("Dezenas por Jogo", 15)

# st.divider()

# Atualização da conferência

st.info(
    "Os concursos utilizados na conferência são definidos individualmente em cada jogo cadastrado."
)

executar = st.button(
    "🔄 Atualizar Conferência",
    width="stretch"
)

# Conferência
if executar:

        resultado = conferir_intervalo(
        df_jogos,
        df_resultados
        )

        st.divider()

        st.subheader("📊 Resumo da Conferência")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Melhor Acerto Geral",
                resultado["Melhor Acerto"].max()
            )

        with col2:
            st.metric(
                "Jogos Conferidos",
                len(resultado)
            )

        with col3:
            st.metric(
            "Concursos Analisados",
            int(
                resultado["Concursos"].max()
            )
        )
            
        st.write("")

        col4, col5, col6 = st.columns(3)

        custo_total = resultado["Custo"].sum()

        valor_recebido_total = resultado[
            "Valor Recebido"
        ].sum()

        resultado_liquido_total = resultado[
            "Resultado Líquido"
        ].sum()

        if custo_total > 0:

            roi_total = (
                resultado_liquido_total
                / custo_total
            ) * 100

        else:

            roi_total = 0

        with col4:
            st.metric(
                "💰 Custo Total",
                formatar_moeda_br(
                    custo_total
                )
            )

        with col5:
            st.metric(
                "💵 Total Recebido",
                formatar_moeda_br(
                    valor_recebido_total
                )
            )

        with col6:
            st.metric(
                "📈 Resultado Líquido",
                formatar_moeda_br(
                    resultado_liquido_total
                ),
                delta=f"{roi_total:.2f}% ROI"
            )

        st.divider()

        st.subheader("📋 Resultado Detalhado")

        resultado_estilizado = (
            resultado
            .set_index("Jogo")
            .style
            .format({
                "Custo": formatar_moeda_br,
                "Valor Recebido": formatar_moeda_br,
                "Resultado Líquido": formatar_moeda_br,
                "Custo Unitário": formatar_moeda_br,
                "ROI %": "{:.2f}%"
            })
            .set_properties(
                **{
                    "text-align": "center"
                }
            )
            .map(
                lambda v: destacar_premiacao(v, "#3b82f6"),
                subset=["11 Pontos"]
            )
            .map(
                lambda v: destacar_premiacao(v, "#22c55e"),
                subset=["12 Pontos"]
            )
            .map(
                lambda v: destacar_premiacao(v, "#eab308"),
                subset=["13 Pontos"]
            )
            .map(
                lambda v: destacar_premiacao(v, "#f97316"),
                subset=["14 Pontos"]
            )
            .map(
                lambda v: destacar_premiacao(v, "#ef4444"),
                subset=["15 Pontos"]
            )
            .map(
                destacar_resultado_liquido,
                subset=["Resultado Líquido"]
            )
        )

        st.dataframe(
            resultado_estilizado,
            width="stretch"
        )

# Jogos carregados
st.divider()

st.subheader("🎯 Jogos Cadastrados")

jogos_estilizados = (
    df_jogos
    .set_index("Jogo")
    .style
    .format(
        lambda x:
        "" if str(x) == "nan"
        else f"{int(x)}"
        if isinstance(x, (int, float))
        else x
    )
    .set_properties(
        **{
            "text-align": "center"
        }
    )
)

st.dataframe(
    jogos_estilizados,
    width="stretch"
)