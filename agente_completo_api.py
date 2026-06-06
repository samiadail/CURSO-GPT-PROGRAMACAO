# Importando bibliotecas e frameworks necessários para o projeto
import streamlit as st
from datetime import datetime
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv
import requests


# Utilizamos para carregar as chaves de API no arquivo ".env"
load_dotenv()


# Criando nossas funções (habilidades/skills)
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"    

    #Estrutura de try/except
    try:
        dados = requests.get(url)
        resposta = dados.json()
        # Estamos convertendo o timestamp (segundos) para uma data legível
        timestamp = resposta['time_last_updated']
        data_convertida = datetime.fromtimestamp(timestamp)
        
        # Conversões (VERIFICAR MOEDA BASE)
        dolar = 1 * resposta['rates']['USD']
        euro = 1 * resposta['rates']['EUR']
        print(data_convertida)

        # Toda função retorna algum valor
        return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} EUR =  1 BRL. Essas informações foram obtidas em {data_convertida}. Quando solicitado, informe que os dados foram atualizados em {data_convertida}"


    except:
        return "Cotação não realizada. Tente novamente"





personalidade = st.sidebar.selectbox(
    "Especialista",
    [
        "Nutricionista",
        "Personal Trainer",
        "Psicólogo",
        "Agente de câmbio"
    ]
)

descricao = {
    "Nutricionista":
        "Você é um nutricionista especializado em alimentação saudável. Sugira receitas e refeições equilibradas.",

    "Personal Trainer":
        "Você é um personal trainer especializado em musculação e cardio. Monte treinos e dê dicas de exercícios.",

    "Psicólogo":
        "Você é um psicólogo especializado em bem-estar mental. Dê dicas sobre estresse e ansiedade.",
        
    "Agente de câmbio":
        "Você é um assistente prestativo de conversão de moedas, que responde sempre com linguagem clara e simples informando o valor da moeda desejada."
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools()],
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
        with st.spinner(f"{personalidade} pensando..."):
            
            
            
            contexto = ""
            
            if personalidade == "Agente de câmbio":
            
                if "dólar" in pergunta.lower() or "dolar" in pergunta.lower() or "euro" in pergunta.lower() or "moedas" in pergunta.lower() or "EURO" in pergunta:

                    contexto = f"O valor atual de conversão de USD e EUR para BRL é: {get_moedas()}"

            
            
            
            
            
            resposta = agente.run(pergunta + contexto)
            st.markdown(resposta.content)

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta.content
        }
    )
    
    