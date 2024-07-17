# Use uma imagem oficial do Python como base
FROM python:3.12

# Instale o pipx e o Poetry
RUN pip install pipx \
    && pipx ensurepath \
    && pipx install poetry

# Configurar o PATH para o Poetry
ENV PATH="/root/.local/bin:${PATH}"

# Copie os arquivos do projeto
COPY . /src

# Defina o diretório de trabalho
WORKDIR /src

# Copie os arquivos de dependências do projeto
# COPY pyproject.toml poetry.lock ./

# Instale as dependências
RUN poetry install

# Exponha a porta usada pelo Streamlit
EXPOSE 8501

# Comando para rodar o aplicativo Streamlit
ENTRYPOINT ["poetry", "run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
