import config
import requests
import time
import json

start = time.time()

with requests.Session() as sessao:

	try:
		respostaPOST = sessao.post(config.LOGIN_URL, data = config.PAYLOAD, headers = config.HEADERS)

		nomeArquivo = "adoteUmCara-API.html"

		respostaGET = []

		for offset in range (1,1000):
			link = config.PRODUCTS_API + str(offset)

			config.HEADERS['Authorization'] = config.AUTHORIZATION_API

			respostaGET = sessao.get(link, headers=config.HEADERS)

			print(offset)

			with open(nomeArquivo, "a") as arquivo:  
				arquivo.write(json.dumps(respostaGET.json())) 


	except Exception as e:
		print (e)


print('TEMPO FINAL:', time.time() - start)