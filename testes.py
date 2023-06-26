import requests
import config
from bs4 import BeautifulSoup

# Resolvemos duas categorias de problemas: Iniciante (1) e Strings (2)
# https://www.beecrowd.com.br/judge/pt/problems/index/<Número Categoria>
# Para acessar os problemas precisamos estar autenticados

# Dados do site
URL_BASE = 'https://www.beecrowd.com.br'
URL_LOGIN = URL_BASE + '/judge/pt/login'

s = requests.Session()

# Obtendo csrfToken
r = s.get(URL_BASE)
soup = BeautifulSoup(r.text, 'html.parser')
csrfToken = soup.find('input', attrs={'name':'_csrfToken'})['value']

# Obtendo _Token só para garantir, vai que muda um dia
token_fields = soup.find('input', attrs={'name':'_Token[fields]'})['value']
token_unlocked = soup.find('input', attrs={'name':'_Token[unlocked]'})['value']

# Criando a requisição de login
login_data = {
    "_csrfToken": csrfToken,
    "email": config.email,
    "password": config.password,
    "remember_me": 0,
    '_Token[fields]': token_fields,
    '_Token[unlocked]': token_unlocked
}

r = s.post(URL_LOGIN, data=login_data)
r = s.get("https://www.beecrowd.com.br/judge/pt/problems/index/1")
soup = BeautifulSoup(r.text, 'html.parser')

