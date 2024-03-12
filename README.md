# CRUD em Django

Este é um projeto Django que implementa um CRUD (Create, Read, Update, Delete) básico para gerenciar uma lista de livros.

## Funcionalidades

- Adicionar um novo livro à lista
- Visualizar a lista de livros
- Editar informações de um livro existente
- Excluir um livro da lista

## Requisitos

- Python 3.11.6
- Django 4.2.11

## Configuração do Ambiente de Desenvolvimento

1. Clone este repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/crud-django.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd crud-django
    ```

3. Crie e ative um ambiente virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações do Django:

    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

7. Abra o navegador e acesse [http://localhost:8000](http://localhost:8000) para visualizar o aplicativo.

## Uso

- Ao acessar [http://localhost:8000](http://localhost:8000), você será redirecionado para a página de listagem de livros.
- Você pode adicionar um novo livro clicando no botão "Adicionar" e preenchendo o formulário.
- Para editar ou excluir um livro existente, clique nos botões "Editar" ou "Excluir" ao lado do livro desejado na lista.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar bugs, sugerir novos recursos ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
