import streamlit as st
import random

st.set_page_config(page_title="Flashcards ETA MS", layout="centered")
st.title("📚 Flashcards sobre Recursos Hídricos")
st.markdown("Pratique seus conhecimentos sobre estações de tratamento de água, qualidade da água e recursos hídricos de Mato Grosso do Sul.")

# Flashcards separados por temas
flashcards = {
    "Mananciais e Recursos Hídricos": [
        {
            "pergunta": "Quais são os dois principais tipos de mananciais usados para abastecimento público?",
            "resposta_correta": "Mananciais superficiais (rios, lagos, represas) e subterrâneos (aquíferos, poços).",
            "alternativas": [
                "Mananciais pluviais (água da chuva) e mananciais costeiros (mar).",
                "Mananciais termais (águas quentes) e mananciais minerais (com sais dissolvidos).",
                "Mananciais salobros (baixa salinidade) e mananciais compostos (mistura de fontes)."
            ]
        },
        {
            "pergunta": "Qual é a bacia hidrográfica que ocupa a maior parte do território de Mato Grosso do Sul?",
            "resposta_correta": "Bacia do Rio Paraná",
            "alternativas": [
                "Bacia do Rio Paraguai",
                "Bacia do Rio Aporé",
                "Bacia do Rio Pardo"
            ]
        },
        {
            "pergunta": "Quais são os principais rios que formam o Pantanal sul-mato-grossense?",
            "resposta_correta": "Rio Paraguai, Rio Taquari, Rio Miranda, Rio Aquidauana e Rio Negro",
            "alternativas": [
                "Rio Paraná, Rio Ivinhema, Rio Pardo, Rio Verde e Rio Sucuriú",
                "Rio Aporé, Rio Santana, Rio Quitéria, Rio Indaiá e Rio Formoso",
                "Rio Coxim, Rio Jauru, Rio Apa, Rio Nabileque e Rio Salobra"
            ]
        },
        {
            "pergunta": "Qual aquífero subterrâneo é um importante reservatório de água doce em Mato Grosso do Sul?",
            "resposta_correta": "Aquífero Guarani",
            "alternativas": [
                "Aquífero Alter do Chão",
                "Aquífero Bambuí",
                "Aquífero Urucuia"
            ]
        }
    ],
    "Qualidade da Água e Parâmetros": [
        {
            "pergunta": "Quais são os principais parâmetros físicos da qualidade da água?",
            "resposta_correta": "Cor, turbidez, temperatura e odor.",
            "alternativas": [
                "pH, dureza, alcalinidade e salinidade.",
                "Oxigênio dissolvido, DBO, DQO e condutividade.",
                "Coliformes, cianobactérias, vírus e protozoários."
            ]
        },
        {
            "pergunta": "O que são coliformes fecais e por que são monitorados?",
            "resposta_correta": "São bactérias indicadoras de contaminação por esgoto e riscos microbiológicos à saúde.",
            "alternativas": [
                "São algas que causam alteração de cor e sabor na água tratada.",
                "São compostos químicos que indicam presença de metais pesados na água.",
                "São minerais que aumentam a dureza da água e prejudicam o tratamento."
            ]
        },
        {
            "pergunta": "Qual parâmetro é considerado crítico no monitoramento de águas do Pantanal sul-mato-grossense durante a estação seca?",
            "resposta_correta": "Oxigênio dissolvido",
            "alternativas": [
                "Temperatura da água",
                "Condutividade elétrica",
                "Radiação solar"
            ]
        },
        {
            "pergunta": "Qual fenômeno natural ocorre em alguns rios de Mato Grosso do Sul que afeta temporariamente a qualidade da água?",
            "resposta_correta": "Dequada (redução do oxigênio dissolvido por decomposição de matéria orgânica)",
            "alternativas": [
                "Eutrofização reversa (redução súbita de nutrientes)",
                "Metalização (aumento natural de metais pesados)",
                "Termalização (aumento excessivo de temperatura)"
            ]
        }
    ],
    "Legislação Ambiental": [
        {
            "pergunta": "O que estabelece a Resolução CONAMA 357/2005?",
            "resposta_correta": "Classifica os corpos d'água segundo seus usos e define padrões de qualidade e limites para lançamento de efluentes.",
            "alternativas": [
                "Define procedimentos para outorga de direito de uso de recursos hídricos.",
                "Estabelece normas para construção de barragens e reservatórios.",
                "Regulamenta a proteção de nascentes e áreas de preservação permanente."
            ]
        },
        {
            "pergunta": "O que caracteriza um corpo d'água de Classe 1 segundo a CONAMA 357?",
            "resposta_correta": "Águas destinadas ao abastecimento público com desinfecção, recreação de contato primário e proteção da vida aquática.",
            "alternativas": [
                "Águas destinadas apenas para navegação e harmonia paisagística.",
                "Águas destinadas exclusivamente para irrigação e dessedentação animal.",
                "Águas que não podem ser utilizadas para nenhum fim devido à contaminação."
            ]
        },
        {
            "pergunta": "O que trata a Resolução CECA 36/2012?",
            "resposta_correta": "Estabelece os critérios e procedimentos para o enquadramento dos corpos d'água do Estado de Mato Grosso do Sul.",
            "alternativas": [
                "Define as taxas de outorga para uso de recursos hídricos em MS.",
                "Regulamenta o licenciamento ambiental de atividades potencialmente poluidoras.",
                "Estabelece diretrizes para recuperação de áreas degradadas no Pantanal."
            ]
        },
        {
            "pergunta": "Qual órgão é responsável pelo monitoramento da qualidade das águas em Mato Grosso do Sul?",
            "resposta_correta": "IMASUL (Instituto de Meio Ambiente de Mato Grosso do Sul)",
            "alternativas": [
                "SANESUL (Empresa de Saneamento de Mato Grosso do Sul)",
                "FUNAI (Fundação Nacional do Índio)",
                "ICMBio (Instituto Chico Mendes de Conservação da Biodiversidade)"
            ]
        },
        {
            "pergunta": "Segundo a legislação estadual, como são classificados os rios da planície pantaneira em MS?",
            "resposta_correta": "Classe 2, com usos múltiplos e exigência de tratamento convencional para abastecimento",
            "alternativas": [
                "Classe Especial, com proteção integral e proibição de qualquer uso",
                "Classe 3, apenas para navegação e dessedentação animal",
                "Classe 4, apenas para harmonia paisagística"
            ]
        }
    ],
    "Estações de Tratamento de Água": [
        {
            "pergunta": "Quais são as etapas clássicas de uma ETA convencional?",
            "resposta_correta": "Coagulação, floculação, decantação, filtração e desinfecção.",
            "alternativas": [
                "Aeração, oxidação, sedimentação, osmose reversa e ozonização.",
                "Peneiramento, neutralização, clarificação, ativação e cloração.",
                "Bombeamento, equalização, precipitação química, adsorção e fluoretação."
            ]
        },
        {
            "pergunta": "O que é o 'jar test' (ensaio de bancada)?",
            "resposta_correta": "Um teste para determinar a dosagem ideal de coagulante na água.",
            "alternativas": [
                "Um teste para verificar a resistência dos frascos usados no laboratório.",
                "Um método para avaliar a durabilidade dos filtros de areia.",
                "Um procedimento para medir a taxa de evaporação nos decantadores."
            ]
        },
        {
            "pergunta": "Quais os principais desafios no tratamento de água proveniente de rios do Pantanal em MS?",
            "resposta_correta": "Alto teor de matéria orgânica e variações sazonais extremas de qualidade",
            "alternativas": [
                "Alta concentração de metais pesados e compostos industriais",
                "Presença de organismos geneticamente modificados",
                "Excesso de compostos radioativos naturais"
            ]
        },
        {
            "pergunta": "Qual tecnologia alternativa é frequentemente utilizada em pequenas comunidades rurais de MS para tratamento de água?",
            "resposta_correta": "Filtração lenta em areia associada à desinfecção solar",
            "alternativas": [
                "Ultrafiltração por membranas pressurizadas",
                "Eletrodiálise reversa com eletrodos de titânio",
                "Troca iônica com resinas poliméricas avançadas"
            ]
        }
    ],
    "Gestão de Recursos Hídricos de MS": [
        {
            "pergunta": "Qual rio forma a divisa entre Brasil e Paraguai, sendo fundamental para a economia de MS?",
            "resposta_correta": "Rio Paraguai",
            "alternativas": [
                "Rio Paraná",
                "Rio Apa",
                "Rio Miranda"
            ]
        },
        {
            "pergunta": "Qual é a importância da hidrovia Paraná-Tietê para Mato Grosso do Sul?",
            "resposta_correta": "Escoamento da produção agrícola e industrial para exportação via Porto de Santos",
            "alternativas": [
                "Abastecimento de água para irrigação nas regiões norte do estado",
                "Captação de água para consumo humano em Campo Grande",
                "Geração de energia elétrica para as pequenas cidades"
            ]
        },
        {
            "pergunta": "Qual problema ambiental tem afetado as nascentes de rios na região leste de MS?",
            "resposta_correta": "Assoreamento devido ao desmatamento e práticas agrícolas inadequadas",
            "alternativas": [
                "Contaminação por mercúrio de garimpos ilegais",
                "Salinização devido à irrigação excessiva",
                "Acidificação por chuvas ácidas industriais"
            ]
        },
        {
            "pergunta": "Qual instrumento de gestão hídrica está previsto no Plano Estadual de Recursos Hídricos de MS?",
            "resposta_correta": "Comitês de Bacias Hidrográficas com participação da sociedade civil",
            "alternativas": [
                "Privatização completa dos serviços de tratamento de água",
                "Proibição de qualquer uso econômico dos recursos hídricos",
                "Cobrança universal por metro cúbico de água da chuva captada"
            ]
        }
    ]
}

# Interface para seleção de tema
if 'tema_selecionado' not in st.session_state:
    st.session_state.tema_selecionado = list(flashcards.keys())[0]

temas = list(flashcards.keys())
tema_selecionado = st.selectbox("Selecione um tema:", temas, index=temas.index(st.session_state.tema_selecionado))
st.session_state.tema_selecionado = tema_selecionado

# Função para embaralhar as alternativas
def embaralhar_alternativas(flashcard):
    todas_opcoes = flashcard["alternativas"].copy()
    todas_opcoes.append(flashcard["resposta_correta"])
    random.shuffle(todas_opcoes)
    return todas_opcoes, todas_opcoes.index(flashcard["resposta_correta"])

# Função para gerar novo flashcard
def novo_flashcard():
    return random.choice(flashcards[st.session_state.tema_selecionado])

# Inicializar estado da sessão
if 'atual' not in st.session_state or st.session_state.tema_selecionado != getattr(st.session_state, 'ultimo_tema', ''):
    st.session_state.atual = novo_flashcard()
    st.session_state.ultimo_tema = st.session_state.tema_selecionado
    st.session_state.opcoes, st.session_state.resposta_index = embaralhar_alternativas(st.session_state.atual)
    st.session_state.respondido = False
    st.session_state.acertos = 0
    st.session_state.total = 0

# Mostrar progresso
st.sidebar.subheader("Seu progresso")
st.sidebar.text(f"Acertos: {st.session_state.acertos}/{st.session_state.total}")
if st.session_state.total > 0:
    taxa_acerto = (st.session_state.acertos / st.session_state.total) * 100
    st.sidebar.progress(taxa_acerto / 100)
    st.sidebar.text(f"Taxa de acerto: {taxa_acerto:.1f}%")

# Exibir pergunta atual
st.markdown(f"### ❓ {st.session_state.atual['pergunta']}")

# Mostrar opções
opcao_selecionada = None
if not st.session_state.respondido:
    opcao_selecionada = st.radio("Escolha a resposta correta:", st.session_state.opcoes, key="opcoes")
    if st.button("Verificar resposta"):
        st.session_state.respondido = True
        st.session_state.total += 1
        if opcao_selecionada == st.session_state.atual["resposta_correta"]:
            st.success("✅ Correto!")
            st.session_state.acertos += 1
        else:
            st.error("❌ Incorreto!")
            st.info(f"A resposta correta é: {st.session_state.atual['resposta_correta']}")
else:
    # Exibir a resposta quando já respondido
    st.info(f"Resposta: {st.session_state.atual['resposta_correta']}")
    if st.button("Próximo Flashcard"):
        st.session_state.atual = novo_flashcard()
        st.session_state.opcoes, st.session_state.resposta_index = embaralhar_alternativas(st.session_state.atual)
        st.session_state.respondido = False

# Reiniciar contador
if st.sidebar.button("Reiniciar progresso"):
    st.session_state.acertos = 0
    st.session_state.total = 0
    st.experimental_rerun()
