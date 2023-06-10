import config
import requests
import time
import json

start = time.time()

with requests.Session() as sessao:

	try:
		respostaPOST = sessao.post(config.LOGIN_URL, data = config.PAYLOAD, headers = config.HEADERS)

		respostaGET = []

		inicio = 1 

		fim = 1002  # range não inclui o ultimo e a ultima pagina é 1001

		pular = 100 # cada pagina tem 100 registros, portanto pra próx pagina pulamos os 100 iniciais


		for offset in range (inicio, fim, pular):
			link = config.PRODUCTS_API + str(offset)

			config.HEADERS['Authorization'] = config.AUTHORIZATION_API

			respostaGET = sessao.get(link, headers=config.HEADERS)

			#só para verificar se o cmd travou
			print(offset)

			with open(config.ARQUIVO_API, "a") as arquivo:  

				arquivo.write(json.dumps(respostaGET.json())) 


	except Exception as e:
		print (e)


print('TEMPO FINAL:', time.time() - start)