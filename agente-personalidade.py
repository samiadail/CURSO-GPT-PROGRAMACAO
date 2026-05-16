from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv


# CARREGAR A CHAVE
load_dotenv()

# CRIO O MODELO DE IA
agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description="Você é um marinheiro, navegador dos 7 mares em busca dos piratas e aventuras",
    markdown = True
)

while True:
    pergunta = input("Digite a sua pergunta: ")

    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente... \n Fique a vontade se tiver mais dúvidas!!!!")
        break
    else:
        agente.print_response(pergunta)
    
    