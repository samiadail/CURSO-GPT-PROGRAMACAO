from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv


# CARREGAR A CHAVE
load_dotenv()

# CRIO O MODELO DE IA
agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    markdown = True
)

while True:
    pergunta = input("Digite a sua pergunta ou digite '0' para encerrar o programa: ")

    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente... \n Fique a vontade se tiver mais dúvidas!!!!")
        break
    else:
        agente.print_response(pergunta)
    
    
        
        
        
        
    # if pergunta != 0:
    #     agente.print_response(pergunta)
            
    # else:
    #     print("Você parou o programa")
        


