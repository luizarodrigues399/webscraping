PAYLOAD = {
	'username': 'SEU_EMAIL_DE_LOGIN_DO_ADOTE',
	'password': 'SUA_SENHA_DO_ADOTE'
	}


# indicar para o site que quem o acessa é um browser real firefox
HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }


# URLS do adote um cara
LOGIN_URL = 'https://www.adoteumcara.com.br/auth/login'

PROFILE_URL = 'https://www.adoteumcara.com.br/profile/'


# limite máximo é 100
PRODUCTS_API = "https://api.adoteumcara.com.br/api/v4/products?fields[user]=basic&page[limit]=100&page[offset]="

AUTHORIZATION_API = 'SUA_BASIC_AUTHORIZATION'

ARQUIVO_API = "dados/adoteUmCara-API.json"

ARQUIVO_IDS = "dados/IDsFinais.txt"

ARQUIVO_FINAL = "dados/adoteUmCara-"