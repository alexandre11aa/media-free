# Media Free

Site agregador de midias gratuitas em Python, Django, Javascript e Bootstrap. É possível acessar o [modelo]() do site hospedado através do PythonAnywhere.

![Media Free](core/static/movies/img/index/media_free_3d_logo.png)

## 🚀 Como executar localmente

**Pré-requisitos**

- Python 3.11.2

**Passos**

1. Clone o repositório:

```shell
$ git clone https://github.com/alexandre11aa/
```

2. Siga para a branch `prod`:

```shell
$ git checkout prod
```

3. Declare um novo `DEBUG` em *core/core/settings.py*:

```python
...
26 # SECURITY WARNING: don't run with debug turned on in production!
27 DEBUG = True
28
...
```

4. Declare um novo `ALLOWED_HOSTS` em *core/core/settings.py*:

```python
...
28
29 ALLOWED_HOSTS = ['*']
30
...
```

5. Siga para o diretório *core/core/* e crie um ambiente virtual:

```shel
$ cd core
$ python3 -m venv env
```

6. Ative o ambiente virtual e instale as dependências:

```shel
$ source env/bin/activate
$ pip install -r requirements.txt
```

7. Faça as migrações do banco de dados:

```shel
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

8. Colete os arquivos estáticos:

```shel
$ python3 manage.py collectstatic
```

9. Inicie o servidor local Django:

```shell
$ python3 manage.py runserver
```

10. Acesse a aplicação no navegador:

```shell
http://localhost:8000
```

## 🌐 Acesso Online

A aplicação está hospedada no PythonAnywhere, podendo ser acessada através de:

🔗 
