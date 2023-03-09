# Projeto Vagas SouJúnior
Projeto de vagas para júnior em TI realizado pela SouJúnior

### Criar Ambiente
`python -m venv venv`

### Instalar Dependências
`pip install -r requirements.txt`

### Run Server
`cd logic`
`python manage.py runserver`

### Admin
Access: http://127.0.0.1:8000/admin

Depois de criar ou modificar um modelo/tabela:
#### create migration files
`python manage.py makemigrations`
#### migrate files to data base
`python manage.py migrate`

### Setup Chromedriver 
#### Ubuntu
`sudo apt-get install chromium-chromedriver` 
### ETL
`cd etl-vagas`
`python execute.py`