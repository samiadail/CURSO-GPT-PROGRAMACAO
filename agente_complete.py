import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox(
    "Especialista",
    [
        "Nutricionista",
        "Personal Trainer",
        "Psicólogo"
    ]
)

descricao = {
    "Nutricionista":
        "Você é um nutricionista especializado em alimentação saudável. Sugira receitas e refeições equilibradas.",

    "Personal Trainer":
        "Você é um personal trainer especializado em musculação e cardio. Monte treinos e dê dicas de exercícios.",

    "Psicólogo":
        "Você é um psicólogo especializado em bem-estar mental. Dê dicas sobre estresse e ansiedade."
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools(), WikipediaTools()],
    markdown=True
)

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if st.sidebar.button("Limpar conversa"):
    st.session_state.mensagens = []
    st.rerun()

st.title("🏥 Clínica Saúde Total")

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Pergunte ao especialista")

if pergunta:

    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        st.markdown(resposta.content)

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta.content
        }
    )