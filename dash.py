import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Função para carregar todos os arquivos Parquet em um diretório
def carregar_parquets(diretorio):
    # Verifica se o diretório existe, caso contrário cria (sem erro se já existir)
    os.makedirs(diretorio, exist_ok=True)
    
    df_list = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".parquet"):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            df_list.append(pd.read_parquet(caminho_arquivo))
    
    return pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()

# Verificar se o DataFrame já foi carregado
if 'df' not in st.session_state:
    # Carregar todos os arquivos Parquet do diretório apenas na primeira vez
    diretorio = "./parquets"  # Mude para o diretório correto
    st.session_state.df = carregar_parquets(diretorio)

# Interface do Streamlit
st.title("Busca de Processos Similares")
st.markdown("### Utilize o campo abaixo para buscar processos por similaridade de texto.")

# Campo para o usuário inserir o texto
texto_dado = st.text_area("Digite o texto para calcular a similaridade", "")

# Botão de busca
if st.button("Buscar Processos Similares"):
    if texto_dado.strip():
        with st.spinner("Carregando dados e processando similaridades..."):
            # Verificar se o DataFrame está vazio
            df = st.session_state.df

            if not df.empty:
                # Verificar se a coluna 'Descricao' existe
                if 'Descricao' in df.columns:
                    # Transformar a coluna 'Descricao' em vetores TF-IDF
                    tfidf_vectorizer = TfidfVectorizer()
                    tfidf_matrix = tfidf_vectorizer.fit_transform(df['Descricao'])

                    # Transformar o texto dado em vetor TF-IDF
                    tfidf_texto_dado = tfidf_vectorizer.transform([texto_dado])

                    # Calcular a similaridade de cosseno entre o texto dado e os textos no dataframe
                    similaridades = cosine_similarity(tfidf_texto_dado, tfidf_matrix)

                    # Adicionar a similaridade ao dataframe
                    df['Similaridade'] = similaridades.flatten()

                    # Ordenar o dataframe pelas similaridades
                    df_ordenado = df.sort_values(by='Similaridade', ascending=False)

                    # Exibir os 5 textos mais similares em um layout organizado e visual
                    st.subheader("Resultados:")
                    st.write(df_ordenado[['Descricao', 'Similaridade']].head(5).style.format({"Similaridade": "{:.2f}"}).background_gradient(cmap="coolwarm"))

                else:
                    st.error("A coluna 'Descricao' não foi encontrada nos dados.")
            else:
                st.error("Nenhum arquivo Parquet foi encontrado no diretório.")
    else:
        st.warning("Por favor, insira um texto para realizar a busca.")

# Rodapé
st.markdown("""
<style>
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
