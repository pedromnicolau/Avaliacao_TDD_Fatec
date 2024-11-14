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
  3a) python -m venv venv
  3b) venv\Scripts\activate
  3c) pip install -r requirements.txt
  3d) cd estagios/
  3e) python manage.py migrate
  3f) python manage.py test
  3g) coverage run --source='.' manage.py test 
  3h) coverage html
  3i) python manage.py runserver
