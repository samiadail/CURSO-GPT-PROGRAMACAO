from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv


# CARREGAR A CHAVE
load_dotenv()

# CRIO O MODELO DE IA
agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description="",
    add_history_to_context=True,
    tools=[DuckDuckGoTools(),TavilyTools],
    markdown = True
)

while True:
    pergunta = input("Digite a sua pergunta: ")

    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente... \n Fique a vontade se tiver mais dúvidas!!!!")
        break
    else:
        agente.print_response(pergunta)
    
    