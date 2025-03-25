# Testes de  nivelamento

## Requisitos

Antes de rodar o projeto, certifique-se de que o [Poetry](https://python-poetry.org/docs/#installation) está instalado. O Poetry é utilizado para gerenciar as dependências e o ambiente virtual do projeto.

## Como instalar o Poetry

Se você ainda não tem o Poetry instalado, recomenda-se a instalação via curl, que é a forma mais confiável para garantir um ambiente isolado:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Caso prefira, também é possível instalar via pip:

```bash
pip install poetry
```

Após a instalação, você pode verificar se o Poetry foi instalado corretamente com o comando:

```bash
poetry --version
```

### Como executar o projeto

1. Instalar as dependências do projeto:

Dentro da pasta do projeto, execute o seguinte comando para instalar todas as dependências listadas no arquivo pyproject.toml:

```bash
poetry install
```
O Poetry irá criar um ambiente virtual e instalar todas as dependências listadas no pyproject.toml.

2. Ativar o ambiente virtual (opcional):

Embora o Poetry gerencie o ambiente automaticamente ao executar os comandos, você pode ativá-lo manualmente com:

Após instalar as dependências, você pode ativar o ambiente virtual com o comando:

```bash
poetry shell
```

Executar o script:

Para executar o script, use o comando abaixo para rodar o arquivo Python dentro do ambiente virtual do Poetry:

```bash
poetry run python scripts/web_scraping.py
```
Ou, se você tiver configurado o Poetry como interpretador no seu editor, pode simplesmente rodar o script diretamente dentro do editor.
4. Verificar onde o ambiente virtual foi criado:

Para verificar o local do ambiente virtual, execute o seguinte comando:

### Verificar onde o ambiente virtual foi criado:
```bash
poetry env info --path
```
