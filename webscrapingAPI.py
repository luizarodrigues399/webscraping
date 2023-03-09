import config
import requests
import time
import json

start = time.time()

with requests.Session() as sessao:

	try:
		respostaPOST = sessao.post(config.LOGIN_URL, data = config.PAYLOAD, headers = config.HEADERS)

		respostaGET = []

		for offset in range (1, 1000):
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