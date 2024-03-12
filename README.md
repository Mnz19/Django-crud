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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# CRUD in Django

This is a Django project that implements a basic CRUD (Create, Read, Update, Delete) to manage a list of books.

## Features

- Add a new book to the list
- View the list of books
- Edit information of an existing book
- Delete a book from the list

## Requirements

- Python 3.x
- Django

## Setting Up Development Environment

1. Clone this repository to your local environment:

    ```bash
    git clone https://github.com/your-username/crud-django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd crud-django
    ```

3. Create and activate a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run Django migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open a web browser and go to [http://localhost:8000](http://localhost:8000) to view the application.

## Usage

- When accessing [http://localhost:8000](http://localhost:8000), you will be redirected to the list of books page.
- You can add a new book by clicking the "Add" button and filling out the form.
- To edit or delete an existing book, click the "Edit" or "Delete" buttons next to the desired book in the list.

## Contributing

Contributions are welcome! Feel free to open an issue to report bugs, suggest new features, or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
