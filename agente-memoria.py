from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv


# CARREGAR A CHAVE
load_dotenv()

bancoDados = SqliteDb(db_file="temp/registros.db")

# CRIO O MODELO DE IA
agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description="Você e um nerd que sabe muito das coisa sobre muitas coisas",
    add_history_to_context=True,
    db=bancoDados,
    session_id="66d49a99-caa6-47af-96c0-dd04a0c839dc",
    num_history_runs=3,
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
    
    