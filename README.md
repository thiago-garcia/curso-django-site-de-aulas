# Site de aulas - Curso Django

Site para postagem de vídeo aulas. Projeto para praticar conteúdo aprendido no curso de Django disponível no repositório [curso-django](https://github.com/thiago-garcia/curso-django). Este projeto foi para aplicar conceitos aprendidos no curso refazendo o código para fixação. Pode conter alterações. 

Projeto desenvolvido com Django e utiliza Pipenv como gerenciador de dependências e Python Decouple para configurações.

Requisitos para executar localmente:

- Git
- Python >= 3.10
- Docker e Docker Compose

Clonar e instalar dependências:

```bash
git clone https://github.com/thiago-garcia/curso-django-site-de-aulas.git
cd curso-django-site-de-aulas
cp contrib/env-sample .env
python -m pip install pipenv
pipenv sync -d
```

Necessário editar a linha do arquivo ```.env``` para ```DEBUG=True```

O projeto utiliza Postgres como banco de dados. Com docker compose, executar:

```bash
docker compose up -d
```

Aplicar migrações no banco de dados e criar usuário:

```bash
# necessário estar no virtualenv, caso não esteja ativo, executar:
pipenv shell 

# aplicar migrações e criar usuário
python manage.py migrate
python manage.py createsuperuser
```

Rodar o servidor localmente:
```bash
# necessário estar no virtualenv, caso não esteja ativo, executar:
pipenv shell 

python manage.py runserver
```