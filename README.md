# Plataforma de Blog com Suporte a Markdown

## Visão Geral
A Plataforma de Blog com Suporte a Markdown é uma aplicação web desenvolvida com Django que permite a criação e visualização de posts utilizando a formatação Markdown. Esta solução simplifica a criação de conteúdo estruturado, permitindo que os autores escrevam seus posts sem precisar lidar com HTML diretamente.

A interface é minimalista e responsiva, focando em proporcionar uma experiência de usuário intuitiva tanto em dispositivos móveis quanto em desktops.

## Tecnologias Utilizadas
- **Django**: Framework Python para desenvolvimento web rápido e seguro.
- **Markdown**: Suporte a Markdown para facilitar a criação de conteúdo formatado.
- **Poetry**: Ferramenta para gerenciamento de dependências e ambiente virtual.
- **Flake8**: Ferramenta de linting para garantir a qualidade do código.
- **CI/CD**: Configuração de Integração Contínua para verificar a qualidade do código a cada commit.

## Funcionalidades
- **Criação de posts**: Adicione novos posts utilizando a sintaxe Markdown para formatação.
- **Lista de posts**: Exibe todos os posts disponíveis.
- **Visualização de post**: Exibe detalhes de um post específico.
- **SEO Amigável**: URLs geradas com base no slug do título do post.
- **Responsividade**: Design adaptado para funcionar bem em qualquer dispositivo.

## Estrutura do Projeto
### Models
- **Post**: Modelo que define um post de blog, com título, conteúdo (Markdown), slug e data de criação.

### Views
- **post_list**: Exibe a lista de posts publicados.
- **post_detail**: Exibe detalhes de um post específico, baseado no slug.

### URLs
- **post_list**: URL para acessar a lista de posts (`/`).
- **post_detail**: URL para acessar o detalhe de um post específico (`/post/<slug>/`).

### Templates
Utiliza o sistema de templates do Django (DTL) para renderizar o conteúdo do blog de forma limpa e estilosa.

## Testes e Qualidade de Código
- **Flake8**: Garante que o código siga as boas práticas do PEP8, detectando problemas de estilo e qualidade.
- **CI/CD**: Configuração de Integração Contínua para executar automaticamente testes e linting ao fazer push no repositório. Isso garante que o código enviado atenda aos padrões de qualidade estabelecidos.

Como Executar o Projeto
Instale o Poetry: Se ainda não tiver o Poetry instalado, siga as instruções de instalação.

Clone o Repositório 

**git clone https://github.com/seu-usuario/blog-platform.git**
cd blog-platform-markdown

**Crie e ative o ambiente virtual: O Poetry gerencia automaticamente o ambiente virtual.**
poetry shell

**Instale as dependênci**
poetry install

**Rode as migrações do banco de dado**
poetry run python manage.py migrate

**Inicie o servidor de desenvolvimento:**
poetry run python manage.py runserver

