# Blog Profissional com Django e Arquitetura de Produção

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen.svg)
![Docker](https://img.shields.io/badge/Docker-20.10-blue.svg)
![Nginx](https://img.shields.io/badge/Nginx-1.29-brightgreen.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3-skyblue.svg)

Este projeto é um blog full-stack construído com Django, com o objetivo principal de ir além do desenvolvimento da aplicação em si, focando na criação e depuração de uma **infraestrutura de produção robusta, escalável e containerizada com Docker.**

O foco deste projeto é demonstrar o conhecimento em todo o ciclo de vida do desenvolvimento de software, desde a configuração do ambiente, passando pela lógica de backend, testes automatizados, fluxo de trabalho de frontend moderno, até a preparação para o deploy.

<img width="1557" height="948" alt="wmp4CRJ" src="https://github.com/user-attachments/assets/fb3d0b57-2808-4746-910a-44b583746c24" />

---

## 🚀 Principais Conceitos e Funcionalidades

Este projeto não é apenas um blog, mas um estudo de caso em arquitetura de software e DevOps.

* **Arquitetura 100% Containerizada com Docker:**
    * Utiliza o **Docker Compose** para orquestrar três serviços principais:
        1.  **Nginx:** Atuando como um **Reverse Proxy** de alta performance, responsável por servir arquivos estáticos e de mídia diretamente, e encaminhar o tráfego dinâmico para a aplicação.
        2.  **Gunicorn:** Como um **Servidor de Aplicação WSGI**, gerenciando os processos da aplicação Django em um ambiente de produção.
        3.  **PostgreSQL:** O banco de dados relacional, rodando em seu próprio contêiner isolado.

* **Fluxo de Trabalho de Frontend Moderno:**
    * Implementação do **Tailwind CSS v3** com um processo de build via `npm`.
    * Configuração do `npm run watch` para **live-reloading** de estilos, permitindo um desenvolvimento de frontend rápido e eficiente sem a necessidade de reiniciar os contêineres.
    * Uso do **DaisyUI** como plugin para acelerar a criação de componentes de UI consistentes.

* **Qualidade de Código e Testes:**
    * Estrutura de testes organizada, separando os testes por funcionalidade (models, views, etc.).
    * Testes unitários e de integração que garantem a estabilidade da aplicação e previnem regressões.

* **Funcionalidades Django:**
    * Sistema de Models completo com relações `ForeignKey` e `ManyToManyField`.
    * Painel de Administração do Django customizado para uma melhor experiência de gerenciamento.
    * Paginação na página inicial utilizando Class-Based Views (`ListView`).
    * Views de detalhe com tratamento de erro 404 (`get_object_or_404`).

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML5, Tailwind CSS, DaisyUI, Node.js/NPM (para o build)
* **Banco de Dados:** PostgreSQL
* **Infraestrutura & DevOps:** Docker, Docker Compose, Nginx, Gunicorn, WSL2

---

## ⚙️ Instalação e Configuração

Siga os passos abaixo para executar o projeto em seu ambiente local.

### Pré-requisitos

* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/) (geralmente já vem com o Docker Desktop)
* [Node.js e NPM](https://nodejs.org/)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/jeanribeir01/blog-django.git
    cd blog-django
    ```

2.  **Crie o arquivo de variáveis de ambiente:**
    * Na pasta `dotenv_files`, renomeie o arquivo `example.env` para `.env`.
    * Abra o `.env` e preencha as variáveis, principalmente a `SECRET_KEY`.

3.  **Instale as dependências do Frontend:**
    ```bash
    npm install
    ```

4.  **Construa e suba os contêineres Docker:**
    ```bash
    docker-compose up --build
    ```
    *A primeira vez pode demorar alguns minutos.*

---

## ▶️ Executando a Aplicação

Para um desenvolvimento eficiente, você precisará de **dois terminais** abertos na raiz do projeto.

1.  **Terminal 1 - Backend:** Inicie todos os serviços do Docker.
    ```bash
    docker-compose up
    ```

2.  **Terminal 2 - Frontend:** Inicie o "vigia" do Tailwind, que irá compilar seu CSS automaticamente a cada alteração.
    ```bash
    npm run watch
    ```

Agora, acesse `http://localhost` no seu navegador!

### Criando um Superusuário

Para acessar o painel de administração (`/admin/`), crie um superusuário com o comando:
```bash
docker-compose exec djangoapp python manage.py createsuperuser
```

---

## ✅ Executando os Testes

Para garantir a qualidade e a integridade da aplicação, execute a suíte de testes:
```bash
docker-compose exec djangoapp python manage.py test
```

---

## 🗺️ Roadmap Futuro

* [ ] Implementação de um sistema de busca para os posts.
* [ ] Criação de um sistema de comentários.
* [ ] Configuração de um pipeline de CI/CD com GitHub Actions para rodar os testes automaticamente.
* [ ] Documentação do processo de deploy em um servidor VPS (ex: DigitalOcean).

---

## 👤 Contato

**Jean Ribeiro**

* LinkedIn: https://www.linkedin.com/in/jeanribeir0/
* Email: jeanribeiro1905@gmail.com

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
