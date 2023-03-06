import datetime
import config
import json


def gerarHTML(resultado, inicio, fim):

	nomeArquivo = "adoteUmCara-" + str(inicio) + '-' + str(fim) +'.html'
	
	# para caso queira imprimir os arquivos sem preocupar com indices de inicio e fim e sem que haja conflito de arquivos
	#tempoCorrente = datetime.datetime.utcnow().timestamp()
	#nomeArquivo = "adoteUmCara-" + str(tempoCorrente)

	with open(nomeArquivo, "a") as arquivo:  

		arquivo.write(json.dumps(resultado)) 



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

	pessoa = conteudo['member']

	# extrai mais dados que o ID para debug/verificação se é mesmo um usuário válido
	dicionario = {
		'id': pessoa['id'],
		'nome': pessoa['pseudo'],
		'titulo': pessoa['title'],
		'idade': pessoa['age'],		
		'cidade': pessoa['city']
	}

	return dicionario

	
def gerarLinks(inicio, fim):

	complemento = []

	print(inicio, ' a ', fim)

	for indice in range(inicio, fim): 

		complemento.append(config.PROFILE_URL + str(indice))

	return complemento


	# return de teste com IDS válidos do site
	#return [
	#	config.PROFILE_URL + '2484532',
	#	config.PROFILE_URL + '2243708',
	#	config.PROFILE_URL + '1'
	#]