from joblib import Parallel, delayed
import funcoes as funcao
import requests
import datetime
import config
import time
import sys

start = time.time()

resultadoFinal = []

#parametros passados por cmd
indiceInicio = int(sys.argv[1])
indiceFim = int(sys.argv[2]) 


def consultaURLExtrairDado(link):
		conteudoPagina = sessao.get(link, headers=config.HEADERS)

		# para debug, se processo congelou ou não.
		print(conteudoPagina, datetime.datetime.now())

		try:
			json = funcao.limparDadosUsuario(conteudoPagina)

			return funcao.extrairFeaturesUsuario(json)

		except:
			pass




""" WITH para fechamento de recurso ou arquivo sem precisar do 
close ou try catch. Independente se der ou não erro, ele fecha"""
with requests.Session() as sessao:

	resposta = sessao.post(config.LOGIN_URL, data = config.PAYLOAD, headers = config.HEADERS)

	urls = funcao.gerarLinks(indiceInicio, indiceFim)


	# verificando quanto tempo demorou a geração de links
	print('GERACAO LINKS:', time.time() - start)

	try:
		resultadoFinal = Parallel(n_jobs = -1, verbose=11) \
			(delayed(consultaURLExtrairDado)(link) for link in urls)

	except:
		pass

	finally:	
		funcao.gerarHTML(resultadoFinal, indiceInicio, indiceFim)


print('TEMPO FINAL:', time.time() - start)