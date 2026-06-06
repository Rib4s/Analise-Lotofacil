import pandas as pd
from modules.config import PRECOS_LOTOFACIL


def converter_moeda(valor):

    if pd.isna(valor):
        return 0.0

    valor = str(valor)

    valor = valor.replace("R$", "")
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    return float(valor.strip())


def contar_acertos(jogo, resultado):
    return len(set(jogo) & set(resultado))


def obter_dezenas_jogo(linha):

    dezenas = []

    for i in range(1, 21):

        coluna = f"D{i}"

        if coluna in linha.index and pd.notna(linha[coluna]):
            dezenas.append(int(linha[coluna]))

    return dezenas


def obter_dezenas_resultado(linha):

    return [
        int(linha[f"Bola{i}"])
        for i in range(1, 16)
    ]


def conferir_intervalo(
    df_jogos,
    df_resultados
):

    resumo = []

    for _, jogo_row in df_jogos.iterrows():

        jogo_numero = int(jogo_row["Jogo"])

        concurso_inicial = int(
            jogo_row["Concurso Inicial"]
        )

        concurso_final = int(
            jogo_row["Concurso Final"]
        )

        resultados_intervalo = df_resultados[
            (df_resultados["Concurso"] >= concurso_inicial)
            &
            (df_resultados["Concurso"] <= concurso_final)
        ]

        dezenas_jogo = obter_dezenas_jogo(
            jogo_row
        )

        melhor_acerto = 0
        melhor_concurso = None

        faixa_11 = 0
        faixa_12 = 0
        faixa_13 = 0
        faixa_14 = 0
        faixa_15 = 0

        valor_recebido = 0.0

        concursos_analisados = len(
            resultados_intervalo
        )

        for _, resultado_row in resultados_intervalo.iterrows():

            dezenas_resultado = obter_dezenas_resultado(
                resultado_row
            )

            acertos = contar_acertos(
                dezenas_jogo,
                dezenas_resultado
            )

            if acertos > melhor_acerto:

                melhor_acerto = acertos

                melhor_concurso = int(
                    resultado_row["Concurso"]
                )

            if acertos == 11:

                faixa_11 += 1

                valor_recebido += converter_moeda(
                    resultado_row["Rateio 11 acertos"]
                )

            elif acertos == 12:

                faixa_12 += 1

                valor_recebido += converter_moeda(
                    resultado_row["Rateio 12 acertos"]
                )

            elif acertos == 13:

                faixa_13 += 1

                valor_recebido += converter_moeda(
                    resultado_row["Rateio 13 acertos"]
                )

            elif acertos == 14:

                faixa_14 += 1

                valor_recebido += converter_moeda(
                    resultado_row["Rateio 14 acertos"]
                )

            elif acertos == 15:

                faixa_15 += 1

                valor_recebido += converter_moeda(
                    resultado_row["Rateio 15 acertos"]
                )

        custo_unitario = PRECOS_LOTOFACIL.get(
            len(dezenas_jogo),
            0
        )

        custo_jogo = (
            custo_unitario
            * concursos_analisados
        )

        resultado_liquido = (
            valor_recebido - custo_jogo
        )

        roi = 0

        if custo_jogo > 0:

            roi = (
                resultado_liquido
                / custo_jogo
            ) * 100

        resumo.append({
            "Jogo": jogo_numero,
            "Qtd Dezenas": len(dezenas_jogo),
            "Concurso Inicial": concurso_inicial,
            "Concurso Final": concurso_final,
            "Concursos": concursos_analisados,
            "Melhor Acerto": melhor_acerto,
            "Melhor Concurso": melhor_concurso,
            "11 Pontos": faixa_11,
            "12 Pontos": faixa_12,
            "13 Pontos": faixa_13,
            "14 Pontos": faixa_14,
            "15 Pontos": faixa_15,
            "Custo Unitário": round(
                custo_unitario,
                2
            ),
            "Custo": round(
                custo_jogo,
                2
            ),
            "Valor Recebido": round(
                valor_recebido,
                2
            ),
            "Resultado Líquido": round(
                resultado_liquido,
                2
            ),
            "ROI %": round(
                roi,
                2
            )
        })

    return pd.DataFrame(resumo)