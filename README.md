# Sistema de Gerenciamento de Laboratório em Django

Este é um sistema Django para gerenciar um laboratório médico, permitindo o agendamento de exames, administração de usuários e controle de tipos de exames.

## Funcionalidades

### Usuário Comum

- Visualizar seus agendamentos de exames.
- Adicionar novos agendamentos de exames.
- Editar e excluir seus agendamentos de exames existentes.

### Administração

- Visualizar todos os agendamentos de exames.
- Filtrar agendamentos por andamento e data.
- Editar e excluir agendamentos de exames.
- Visualizar e gerenciar usuários (exceto administradores).
- Visualizar, adicionar, editar e excluir tipos de exames.

## Requisitos

- Python 3.11.6
- Django 4.2.11

## Configuração do Ambiente de Desenvolvimento

1. Clone este repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/sistema-laboratorio-django.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd sistema-laboratorio-django
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

### Usuário Comum

- Ao acessar [http://localhost:8000](http://localhost:8000), você poderá visualizar seus agendamentos de exames.
- Para adicionar um novo agendamento de exame, clique no botão "Adicionar" e preencha o formulário.
- Para editar ou excluir um agendamento de exame existente, clique nos botões "Editar" ou "Excluir" ao lado do agendamento desejado na lista.

### Administração

- Para acessar a área de administração, você precisa estar autenticado como superusuário.
- Acesse [http://localhost:8000/admin](http://localhost:8000/admin) e faça login com suas credenciais de superusuário.
- Você será redirecionado para a página de administração, onde poderá visualizar todos os agendamentos de exames, gerenciar usuários e tipos de exames.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar bugs, sugerir novos recursos ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


---------------------------------------------------------------------
# Laboratory Management System in Django

This is a Django system for managing a medical laboratory, allowing for scheduling of exams, user administration, and control of exam types.

## Features

### Common User

- View their scheduled exams.
- Add new exam appointments.
- Edit and delete their existing exam appointments.

### Administration

- View all exam appointments.
- Filter appointments by status and date.
- Edit and delete exam appointments.
- View and manage users (except administrators).
- View, add, edit, and delete exam types.

## Requirements

- Python 3.11.6
- Django 4.2.11

## Setting Up Development Environment

1. Clone this repository to your local environment:

    ```bash
    git clone https://github.com/your-username/lab-management-django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd lab-management-django
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

### Common User

- Upon accessing [http://localhost:8000](http://localhost:8000), you can view your scheduled exams.
- To add a new exam appointment, click the "Add" button and fill out the form.
- To edit or delete an existing exam appointment, click the "Edit" or "Delete" buttons next to the desired appointment in the list.

### Administration

- To access the administration area, you need to be authenticated as a superuser.
- Go to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with your superuser credentials.
- You will be redirected to the administration page, where you can view all exam appointments, manage users, and exam types.

## Contributing

Contributions are welcome! Feel free to open an issue to report bugs, suggest new features, or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

