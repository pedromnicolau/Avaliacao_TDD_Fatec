# Avaliacao_TDD_Fatec

Professor: Orlando Saraiva Jr

Matéria: Desenvolvimento de software 3

Linguagem utilizada: Python

Framework utilizado: Django

Nessa avaliação, o professor disponibilizou uma CRUD básico de vagas de estágio com os campos titulo, empresa e telefone, e foi requisitada a implementação de dois novos campos: email e descricao, além das alterações necessárias nos testes do projeto.

Para rodar o projeto:

1- Instale o Python em sua máquina

2- Abra o terminal e clone o repositório

3- Rode os comandos:

    3.1) python -m venv venv

    3.2) venv\Scripts\activate

    3.3) pip install -r requirements.txt

    3.4) cd estagios/

    3.5) python manage.py migrate

    3.6) python manage.py test

    3.7) coverage run --source='.' manage.py test
 
    3.8) coverage html

    3.9) python manage.py runserver
