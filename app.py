import streamlit as st
import requests
import extra_streamlit_components as stx

st.title("Ofertas personalizadas por cliente")

if 'nome' not in st.session_state:
    st.session_state.nome = ""

if 'data' not in st.session_state:
    st.session_state.data = []

if 'mensagem' not in st.session_state:
    st.session_state.mensagem = []

nome = st.text_input("Por favor, insira o código do cliente para prosseguir.")

try:
    if st.session_state.nome != nome:
        print('teste1')
        st.session_state.nome = nome 

        data = []
        mensagem = []

        with st.spinner('Carregando recomendações...'):
            
                url = f'https://recomendacao-produtos.onrender.com/recomendar/produtos/{nome}'
                response = requests.get(url)
                if response.status_code == 200:
                    dados = response.json()
            

        for index, nome in enumerate(dados['produtos']):
            data.append(stx.TabBarItemData(id=index, title=f'Oferta {index+1}', description=nome))
            mensagem.append(dados['oferta'][index]['mensagem'])

        st.session_state.data = data
        st.session_state.mensagem = mensagem
        
    if len(st.session_state.mensagem) > 0:
        index_selecionado = stx.tab_bar(data=st.session_state.data, default=0)
        st.info(st.session_state.mensagem[int(index_selecionado)])
except Exception as e:
    st.error(f"Ocorreu um erro ao buscar as recomendações.")