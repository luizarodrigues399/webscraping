<h3> Finalidade </h3>
<p> Esse projeto visa fazer um webscraping dos perfis de pessoas do site de relacionamento Adote Um Cara. </p>
<p> Ele foi testado e construido usando Python 3.11.2, rodando em Windows 10 com 8 Giga de RAM e processador Intel CORE i7. </p>

<p> Data de release da pasta: 09/03/2023.</p>

##  

<h3> Detalhamento </h3>
<p> Esse projeto consiste de 4 arquivos principais:
<ul>
  <li> Um arquivo de webscraping que roda em sequencial, mais lento; </li>
  <li> Um arquivo em paralelo, usando o máximo de workers que o desktop pode disponibilizar, atrelado a um arquivo chamado bash.sh, em que o usuário insere a posição inicial e final do array de IDs pra pegar quais IDs de usuário ele quer testar;</li>
  <li> Um arquivo webscraping que usa do endpoint do Adote um Cara para fazer requisições; </li>
  <li> Um arquivo webscraping que usa do endpoint do Adote um Cara para fazer requisições, porém em javascript. </li>
</ul>

<p> Rode primeiramente um dos dois arquivos: webscrapingJavascript.js ou webscrapingAPI.py. Ambos tem a mesma função de retornar os IDs válidos dos usuários para montar a URL. </p>
<p> O arquivo webscrapingJavascript.js é para ser executado copiando e colando dentro do browser no site do Adote um Cara, com seu usuário logado, enquanto o arquivo webscrapingAPI só precisa rodar normalmente como .py
</p>

<p> Após, use o arquivo LimpezaDados, que possui um jeito de "limpar" o resultado dos dois arquivos anteriores, pois irá voltar outros dados que não precisaremos no momento.</p>

<p> Use um dos dois arquivos (webscrapingParalelo ou webscrapingSequencial) para realmente coletar os dados de cada URL.</p>

<p> O webscraping sequencial e paralelo funcionam via força bruta, passando link por link. </p>

<p> O webscraping paralelo utiliza-se do poder de vários workers juntamente com vários processos. Para tal, ao abrir o bash.sh, após configurar os parametros, vários processos irão se abrir no desktop. Pode-se colocar em background, mas por questões de debug, resolvi deixá-los visiveis.</p>

<p> O arquivo gerarBashComandos.py gera de forma mais fácil indices de parametros para o arquivo bash.sh, pra não precisar ficar colocando na mão.</p>


<p> Na pasta exemplos possui o webscraping de 2 perfis reais, em formato de json, e um webscraping da página inteira de um perfil real. </p>

<p>OBS 1: Para os arquivos que utilizam os endpoints do Adote, vale ressaltar que o Adote um Cara não possui documentação de API facilmente acessada por terceiros (provavelmente os endpoints são apenas internos ao sistema ou parceiros comerciais deles).</p>

<p>OBS 2: Sugiro utilizar Postman para analisar outras requisições da API do Adote um Cara. </p>



