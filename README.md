# Projeto Web - Django

Repositório inicial do projeto para a disciplina de Programação Web.

## Tecnologias
- Python 3
- Django 5
- Git & GitHub

## Estrutura de Branches (GitFlow Simplificado)
- `main` → código final e estável  
- `develop` → branch de desenvolvimento  
- `feature/nadin-setup` → branch da Nadin para configuração inicial  

membros do grupo devem criar suas próprias branches:  
`feature/nome-da-pessoa`.



## Como rodar o projeto


### 1. Clonar o repositório

git clone https://github.com/nadii91/projeto-web

cd projeto-web


### 2. Criar ambiente virtual:

python -m venv venv


### 2. Ativar ambiente virtual:
Windows:

venv\Scripts\activate

###

### 3. Instalar dependências:

pip install -r requirements.txt


### 4. Rodar as migrações

python manage.py migrate



### 5. Rodar o servidor:

python manage.py runserver


### 6. Acessar no navegador:

http://127.0.0.1:8000/
