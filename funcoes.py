import datetime
import config
import json


def gerarHTMLDateTime(resultado):
	
	tempoCorrente = datetime.datetime.utcnow().timestamp()

	nomeArquivo = config.ARQUIVO_FINAL + str(tempoCorrente) + '.json'

	with open(nomeArquivo, "a") as arquivo:  

		arquivo.write(json.dumps(resultado)) 


def gerarHTML(resultado, inicio, fim):

	nomeArquivo = config.ARQUIVO_FINAL + str(inicio) + '-' + str(fim) +'.json'
	
	with open(nomeArquivo, "a") as arquivo:  

		arquivo.write(json.dumps(resultado)) 



def gerarLinks(arquivo, inicio, fim):

	with open(arquivo, "r") as arquivo:  
		resultado = arquivo.read()

		resultado = resultado.split(',')

		return resultado[inicio:fim]



def limparDadosUsuario(conteudoPagina):

	texto = conteudoPagina.text

	# palavras/frases unicas
	comecoDados = texto.find('window.profileData')

	fimDados = texto.find("window.modules.charmsCarousel = true;")

	texto = texto[comecoDados:fimDados]

	# remove lixo
	texto = texto[texto.find('{') : ]

	texto = texto[ : texto.find(';')]


	#transforma os dados em json
	return json.loads(texto)


def printJson(conteudo):

	print(json.dumps(conteudo, indent=4))



def extrairFeaturesUsuario(conteudo):

	membro = conteudo['member']
	headingBlock = conteudo['headingBlock']
	mapa = conteudo['sideColumn']['map'] 

	dicionario = {
		'id': membro['id'],
		'nome': membro['pseudo'],
		'titulo': membro['title'],
		'idade': membro['age'],		
		'cidade': membro['city'],
		'fotoPerfil': membro['covers'][0],
		'fotos': membro['pictures'],
		'ultimaConexao': headingBlock['lastConnection'],
		'hashtags': headingBlock['hashtags'],
		'popularidade': headingBlock['popularity']['popu'],
		'detalhamentoPerfil': conteudo['mainColumn'],
		'latitude': mapa['coords']['memberLat'],
		'longitude': mapa['coords']['memberLng']
	}

	return dicionario

	
