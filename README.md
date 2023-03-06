<h3> Finalidade </h3>
<p> Esse projeto visa fazer um webscraping dos perfis de pessoas do site de relacionamento Adote Um Cara, para servir de database para meu projeto de TCC. </p>
<p> Ele foi testado e construido usando Python 3.11.2, rodando em Windows 10 com 8 Giga de RAM e processador Intel CORE i7. </p>

##  

<h3> Detalhamento </h3>
<p> Esse projeto consiste de 4 arquivos:
<ul>
  <li> Um arquivo de webscraping que roda em sequencial, mais lento; </li>
  <li> Um arquivo em paralelo, usando o máximo de workers que o desktop pode disponibilizar, também usando de um arquivo chamado bash.sh, em que o usuário insere de qual link até qual número do link ele quer testar;</li>
  <li> Um arquivo webscraping que usa do endpoint do Adote um Cara para fazer requisições; </li>
  <li> Um arquivo webscraping que usa do endpoint do Adote um Cara para fazer requisições, porém em javascript. </li>
</ul>

<p> O motivo para o qual existem tem 4 formas de webscraping com o mesmo objetivo, foi a constante busca da melhora do scraping (ou seja, comecei com o sequencial, coloquei o scraping em paralelo e por fim descobri e analisei os endpoints do site, tudo visando conseguir o maior número de links válidos no menor tempo).</p>

<p> O webscraping sequencial e paralelo funcionam via força bruta, passando link por link. </p>

<p> O webscraping paralelo utiliza-se do poder de vários workers juntamente com vários processos. Para tal, ao abrir o bash.sh, após configurar os parametros e descomentar as linhas comentadas, vários processos irão se abrir no desktop. Pode-se colocar em background, mas por questões de debug, resolvi deixá-los visiveis.</p>

<p> Para 10 mil links analisados, o webscraping paralelo demora em torno de 20 a 30 minutos, com 10 processos abertos simultaneamente, cada um com um parametro diferente. </p>

<p> Para o arquivo que utiliza o endpoint do Adote, vale ressaltar que o Adote um Cara não possui documentação de API (provavelmente os endpoints são apenas internos ao sistema).</p>

<p>Sugiro utilizar Postman para analisar outras requisições da API do Adote um cara. </p>

<p> Os arquivos que usam endpoints do site se diferem entre si pela URL em que buscam os dados e a forma de execução: o arquivo webscrapingJavascript é para ser executado copiando e colando dentro do browser no site do adote, com seu usuário logado, enquanto o arquivo webscrapingAPI, so precisa rodar normalmente como .py </p>




