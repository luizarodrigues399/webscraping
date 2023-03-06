import funcoes as funcao
import requests
import config
import time
import sys


start = time.time()

resultadoFinal = []

indiceInicio = int(sys.argv[1])
indiceFim = int(sys.argv[2]) 


""" WITH para fechamento de recurso ou arquivo sem precisar do 
close ou try catch. Independente se der ou não erro, ele fecha"""
with requests.Session() as sessao:

	sessao.post(config.LOGIN_URL, data = config.PAYLOAD, headers = config.HEADERS)

	urls = funcao.gerarLinks(indiceInicio, indiceFim)

	for link in urls:
		print(link)

		conteudoPagina = sessao.get(link, headers = config.HEADERS)

		try:
			json = funcao.limparDadosUsuario(conteudoPagina)

			resultadoFinal.append(funcao.extrairFeaturesUsuario(json))

		except:
			pass

	funcao.gerarHTML(resultadoFinal, indiceInicio, indiceFim)


end = time.time()

print('TEMPO:', end - start)