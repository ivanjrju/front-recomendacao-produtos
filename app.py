import streamlit as st
import requests
import extra_streamlit_components as stx

# Título da aplicação
st.title("Ofertas personalizadas por cliente")

# Campo de input
nome = st.text_input("Por favor, insira o código do cliente para prosseguir.")



# Verifica se o usuário inseriu algo
if nome:
    url = f'https://recomendacao-produtos.onrender.com/recomendar/produtos/{nome}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()

    data = []
    mensagem = []
    for index, nome in enumerate(dados['produtos']):
        data.append(stx.TabBarItemData(id=index, title=f'Oferta {index+1}', description=nome))
        mensagem.append(dados['oferta'][index]['mensagem'])

    print(mensagem)

    index_selecionado = stx.tab_bar(data=data, default=0)
    print(index_selecionado)
    st.info(mensagem[int(index_selecionado)])

    