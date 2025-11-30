# Media Free

Site agregador de midias gratuitas em Python, Django, Javascript e Bootstrap. É possível acessar o [caminho](https://mediafree.pythonanywhere.com/) do site hospedado através do PythonAnywhere.

![Media Free](core/static/movies/img/index/media_free_3d_logo.png)

## 🚀 Como executar localmente

**Pré-requisitos**

- Python 3.11.2

**Passos**

1. Clone o repositório:

```shell
$ git clone https://github.com/alexandre11aa/media-free.git
```

2. Declare um novo `DEBUG` em *core/core/settings.py*:

```python
...
26 # SECURITY WARNING: don't run with debug turned on in production!
27 DEBUG = True
28
...
```

3. Declare um novo `ALLOWED_HOSTS` em *core/core/settings.py*:

```python
...
28
29 ALLOWED_HOSTS = ['*']
30
...
```

4. Siga para o diretório *core/core/* e crie um ambiente virtual:

```shel
$ cd core
$ python3 -m venv env
```

5. Ative o ambiente virtual e instale as dependências:

```shel
$ source env/bin/activate
$ pip install -r requirements.txt
```

6. Faça as migrações do banco de dados:

```shel
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

7. Colete os arquivos estáticos:

```shel
$ python3 manage.py collectstatic
```

8. Inicie o servidor local Django:

```shell
$ python3 manage.py runserver
```

- Acesse a aplicação no navegador:

```shell
http://localhost:8000
```

## 🌐 Acesso Online

A aplicação está hospedada no PythonAnywhere, podendo ser acessada através de:

🔗 https://mediafree.pythonanywhere.com/
