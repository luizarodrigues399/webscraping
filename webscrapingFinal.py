from joblib import Parallel, delayed
import requests
import config
import funcao
import time
import json


start = time.time()

resultadoFinal = []

	
def gerarLinks():

	nomeArquivo = "IDsFinais.txt"

	with open(nomeArquivo, "r") as arquivo:  
		resultado = arquivo.read()

		resultado = resultado.split(',')

		return resultado[0:3]

def gerarTXT(resultado):

	nomeArquivo = "adoteUmCaraFinal.txt"

	with open(nomeArquivo, "a") as arquivo:  

		arquivo.write(json.dumps(resultado)) 


def consultaURLExtrairDado(link):
		conteudoPagina = sessao.get(config.PROFILE_URL + link, headers = config.HEADERS)

		# para debug, se processo congelou ou não.
		print(conteudoPagina, datetime.datetime.now())

		try:
			return funcao.extrairFeaturesUsuario(json)

		except:
			pass


with requests.Session() as sessao:

	resposta = sessao.post(config.LOGIN_URL, data = config.PAYLOAD, headers = config.HEADERS)

	urls = gerarLinks()

	try:
		
		
		#resultadoFinal = Parallel(n_jobs = -1, verbose=11) \
		#	(delayed(consultaURLExtrairDado)(config.PROFILE_URL + link) for link in urls)

	except:
		pass

	finally:	
		gerarTXT(resultadoFinal)



end = time.time()

print('TEMPO:', end - start)