import streamlit as st

            # PAGINA WEB 
# st.title("Bem Vindo à minha primeira página WEB")
# st.subheader("Desenvolvido por: SAMI")

# nome = st.text_input("Digite o seu nome: ")

# if nome:
#     st.success(f"Bem Vindo: {nome}")
#     st.balloons()
            # ------------
            
            
            
            # SISTEMA DE CONTRATAÇÃO RH
            
st.title("Bem-vindo ao Sistema Virtual de Contratação")
st.subheader("Por favor colocar suas informações abaixo: ")


nome = st.text_input("Digite o seu nome: ")

email = st.text_input("Digite o seu email: ")

botao = st.button("Cadastrar")

if botao:

    if nome and email:
        st.success(f"Seu Cadastro ficou salvo com {nome}")
        st.success(f"Seu Cadastro ficou salvo com {email}")
        st.snow()
    else:
        st.error("Você ainda não completou todos os dados do cadastro")
    


