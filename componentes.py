import streamlit as st



            # SENAI SITE 
            
            
st.title("Secretaria SENAI Americana")
st.header("Conheça os nossos cursos")

st.write("I.A. Generativa, Power BI, Empilhadeira, Excel, Eletricista Instalador ")

st.markdown("**Atenção**: Verifique se existem vagas disponíveis.")

nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Digite a sua idade", min_value=16, max_value=99)

cursoEscolhido = st.selectbox("Cursos disponíveis", ["I.A. Generativa", "Power BI", "Empilhadeira", "Excel", "Eletricista Instalador"])

aceitaTermos = st.checkbox("Ao clicar aki, você aceita os termos de condiçôes")

if st.button("Enviar respota"):
    if nome and idade and cursoEscolhido and aceitaTermos:
        st.success(f"Olá, {nome}, Você tem {idade} anos, você escolheu o curso {cursoEscolhido}, e aceitou os temos de condição.")
        
    else:
        st.error("Você ainda não completou todos os seus dados.")

            # --------------------------
            
            # SITE DA PIZZARIA PADRE MAS EU JA MOVI PARA OUTRO ARTQUIVO
            
# st.title("Pizzaria PADRE")
# st.image("pizza.jpg")
# st.header("Conheça as nossas melhores e diversas pizzas.🍕🍕🍕")


# st.markdown("**Complete a pesquisa**")

# nome = st.text_input("Digite o seu nome: 🧍")
# cidade = st.text_input("Digite a sua cidade: 🏙️")
# bairro = st.text_input("Digite o seu bairro: 🏡")




# cursoEscolhido = st.selectbox("Escolha o sabor da sua pizza", ["Pizza de Calabresa", "Pizza de Frango com Catupiry", "Pizza Portuguesa", "Pizza de Margherita", "Pizza de Pepperoni"])

# aceitaTermos = st.checkbox("Ao clicar aki, você aceita os termos de condiçôes")

# if st.button("Enviar pesquisa"):
#     if nome and cidade and bairro and aceitaTermos:
#         st.success(f"Olá, {nome}, Você é de {cidade}, do bairro {bairro}, e aceitou os temos de condição.")
        
#     else:
#         st.error("Você ainda não completou todos os seus dados.")

            # ------------------------------