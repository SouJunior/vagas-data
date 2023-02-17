# Importar bibliotecas
import requests
import os
from selenium import webdriver

URL_VAGAS = 'https://www.linkedin.com/jobs/search/?currentJobId=3476962522&f_E=1%2C2%2C3&f_I=4%2C96%2C3105&keywords=junior&refresh=true&sortBy=R'

BASE_PATH = os.path.abspath(__file__ + '/../')
DATA_PATH = f'{BASE_PATH}/data/'
HTML_PATH = DATA_PATH + 'html/'

def criar_pasta_caso_inexistente(path):
    """
    Conferir existência de pasta sem sobrescrever
    """
    print(f'Criando pasta: {path}')
    os.makedirs(os.path.dirname(path), exist_ok=True)

def criar_pasta():
    criar_pasta_caso_inexistente(HTML_PATH)

#TODO: criar_lista_vagas

#TODO: capturar_vagas

# Função principal executada no script execute.py
def main():
    print('[Extract] start')
    criar_pasta()
    print('[Extract] end')

