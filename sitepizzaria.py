import streamlit as st

st.title("Pizzaria PADRE")
st.image("pizza.jpg")
st.header("Conheça as nossas melhores e diversas pizzas.🍕🍕🍕")

# st.write("I.A. Generativa, Power BI, Empilhadeira, Excel, Eletricista Instalador ")

st.markdown("**Complete a pesquisa**")

nome = st.text_input("Digite o seu nome: 🧍")
cidade = st.text_input("Digite a sua cidade: 🏙️")
bairro = st.text_input("Digite o seu bairro: 🏡")




cursoEscolhido = st.selectbox("Escolha o sabor da sua pizza", ["Pizza de Calabresa", "Pizza de Frango com Catupiry", "Pizza Portuguesa", "Pizza de Margherita", "Pizza de Pepperoni"])

aceitaTermos = st.checkbox("Ao clicar aki, você aceita os termos de condiçôes")

if st.button("Enviar pesquisa"):
    if nome and cidade and bairro and aceitaTermos:
        st.success(f"Olá, {nome}, Você é de {cidade}, do bairro {bairro}, e aceitou os temos de condição.")
        
    else:
        st.error("Você ainda não completou todos os seus dados.")