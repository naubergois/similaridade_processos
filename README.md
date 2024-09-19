
# Projeto de Dashboard Streamlit

Este projeto contém um dashboard desenvolvido com [Streamlit](https://streamlit.io/) para buscar processos similares utilizando a técnica de TF-IDF e calcular similaridade de cosseno entre textos. O projeto também carrega automaticamente arquivos Parquet de um diretório especificado e permite que o usuário insira um texto para realizar buscas por similaridade.

## Estrutura do Projeto

- `dash.py`: Script principal que contém o código para execução do dashboard Streamlit. Este script carrega arquivos Parquet do diretório `./parquets`, transforma as descrições de processos em vetores TF-IDF e calcula a similaridade de cosseno com base no texto fornecido pelo usuário.
  
- `Notebook1.ipynb`: Notebook contendo exemplos de execução e possíveis testes. Pode incluir código de pré-processamento ou experimentos com os dados.

## Requisitos

- Python 3.7 ou superior
- Dependências listadas no arquivo `requirements.txt` ou os seguintes pacotes Python:

  ```bash
  pip install streamlit pandas scikit-learn
  ```

## Como executar o projeto

1. **Clone o repositório** ou baixe os arquivos.

2. **Instale as dependências**:

   Execute o seguinte comando para instalar as dependências necessárias para o projeto:

   ```bash
   pip install -r requirements.txt
   ```

   Se o arquivo `requirements.txt` não estiver disponível, instale as dependências manualmente com:

   ```bash
   pip install streamlit pandas scikit-learn
   ```

3. **Execute o dashboard**:

   Navegue até o diretório onde está o arquivo `dash.py` e execute o comando:

   ```bash
   streamlit run dash.py
   ```

4. **Acessar o Dashboard**:

   Após a execução, o Streamlit fornecerá um link (algo como `http://localhost:8501`), que você pode abrir no navegador para visualizar e interagir com o dashboard.

## Funcionalidades

- **Carregamento de Arquivos Parquet**: O dashboard carrega automaticamente todos os arquivos `.parquet` do diretório `./parquets`. Caso o diretório não exista, ele será criado.
  
- **Busca por Similaridade**: O usuário pode inserir um texto e o dashboard irá buscar processos similares com base em similaridade de cosseno calculada a partir da técnica TF-IDF.

- **Resultado Visual**: Os 5 processos mais similares são exibidos em uma tabela estilizada com destaque para os níveis de similaridade.

## Observações

- O diretório `./parquets` deve conter arquivos `.parquet` com uma coluna chamada `Descricao`, que será usada para calcular a similaridade de textos.
- Certifique-se de que os arquivos `.parquet` estejam no formato correto para que o sistema funcione adequadamente.

---

### Contato

Para dúvidas ou sugestões, entre em contato com o desenvolvedor.
