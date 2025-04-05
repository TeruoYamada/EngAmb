import streamlit as st
import random

st.set_page_config(page_title="Flashcards ETA", layout="centered")

st.title("📚 Flashcards sobre ETA e Qualidade da Água")
st.markdown("Pratique seus conhecimentos sobre estações de tratamento de água e normas ambientais como CONAMA 357 e CECA 36/12.")

flashcards = [
    ("Quais são os dois principais tipos de mananciais usados para abastecimento público?", "Mananciais superficiais (rios, lagos, represas) e subterrâneos (aquíferos, poços)."),
    ("Cite três critérios importantes para escolher um manancial.", "Qualidade da água, quantidade disponível (vazão mínima garantida), proximidade da população atendida."),
    ("Quais são os principais parâmetros físicos da qualidade da água?", "Cor, turbidez, temperatura e odor."),
    ("O que são coliformes fecais e por que são monitorados?", "São bactérias indicadoras de contaminação por esgoto e riscos microbiológicos à saúde."),
    ("O que estabelece a Resolução CONAMA 357/2005?", "Classifica os corpos d’água segundo seus usos e define padrões de qualidade e limites para lançamento de efluentes."),
    ("O que caracteriza um corpo d’água de Classe 1 segundo a CONAMA 357?", "Águas destinadas ao abastecimento público com desinfecção, recreação de contato primário e proteção da vida aquática."),
    ("Qual o limite de concentração de coliformes termotolerantes para rios Classe 2?", "1000 NMP/100 mL em 80% ou mais das amostras mensais, num período de 12 meses."),
    ("O que é considerado poluição difusa segundo a CONAMA 357?", "Poluição proveniente de várias fontes pequenas e não pontuais, como escoamento agrícola ou urbano."),
    ("O que trata a Resolução CECA 36/2012?", "Estabelece os critérios e procedimentos para o enquadramento dos corpos d’água do Estado de Mato Grosso do Sul."),
    ("O que é 'enquadramento dos corpos d’água'?", "É a definição dos usos desejados para um corpo hídrico e a qualidade que ele deve manter para esses usos."),
    ("Segundo a CECA 36/12, qual a prioridade no uso da água?", "Abastecimento humano com qualidade compatível e sem tratamento complexo."),
    ("Que instrumento de gestão a CECA 36/12 complementa?", "O Plano Estadual de Recursos Hídricos e a Política Nacional de Recursos Hídricos."),
    ("Quais são as etapas clássicas de uma ETA convencional?", "Coagulação, floculação, decantação, filtração e desinfecção."),
    ("O que é o 'jar test' (ensaio de bancada)?", "Um teste para determinar a dosagem ideal de coagulante na água."),
    ("Quais os coagulantes mais usados no Brasil?", "Sulfato de alumínio e policloreto de alumínio (PAC)."),
    ("Qual é o objetivo da filtração na ETA?", "Remover partículas pequenas e microorganismos não decantados."),
    ("Por que a desinfecção é importante na ETA?", "Para eliminar microorganismos patogênicos e garantir segurança à saúde."),
    ("Quais os principais fatores para dimensionar uma ETA?", "População futura, consumo per capita, qualidade da água bruta e vazões de projeto."),
    ("O que significa vazão de projeto?", "É a vazão máxima prevista para o período de vida útil da ETA, considerando o crescimento populacional."),
    ("O que deve ser considerado ao escolher o local da ETA?", "Acessibilidade, topografia, proximidade ao manancial e área para ampliação futura.")
]

# Embaralhar flashcards
def novo_flashcard():
    return random.choice(flashcards)

if 'atual' not in st.session_state:
    st.session_state.atual = novo_flashcard()

pergunta, resposta = st.session_state.atual

st.markdown(f"### ❓ {pergunta}")

if st.button("Mostrar Resposta"):
    st.info(resposta)

if st.button("Próximo Flashcard"):
    st.session_state.atual = novo_flashcard()
    st.experimental_rerun()
