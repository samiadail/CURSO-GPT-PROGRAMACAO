import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

agente = Agent( # Tupla POIS NÃO MUDAREMOS OS PARÂMETROS DO AGENTE 
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um chefe de cozinhada muito renomado, mas você é focado na área da culinaria brasileira.",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)


st.title("Agente de I.A. 🤖")

pergunta = st.chat_input("Digite sua pergunta")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
        with st.chat_message("assistant"):
            with st.spinner("Agente pensando..."):
                respostas = agente.run(pergunta)
                st.markdown(respostas.content)
            
            