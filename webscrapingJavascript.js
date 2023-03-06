// copiar esse código e colar no browser do adoteUmCara, enquanto logado no sistema, em qualquer página interna
// Baseado em: https://stackoverflow.com/questions/21012580/is-it-possible-to-write-data-to-file-using-only-javascript   


// os valores de offsets são os mesmos encontrados ao chamar a URL no site
var offsets = [15, 27, 39, 51, 63, 75];

var headers = { 
      'Authorization': 'SUA_BASIC_AUTHORIZATION'
};

offsets.forEach(function (offset){
   
    $.ajax({

      url: "https://www.adoteumcara.com.br/mySearch/more?offset=" + offset + "&count=1000",

      headers: headers,
    })
      .done(function(dados) {

        console.log( "Sample of data:", dados );


        var textFile=null, makeTextFile = function (text) {

                var data = new Blob([text], {type: 'text/plain'});
            
                if (textFile !== null) {
                  window.URL.revokeObjectURL(textFile);
                }
            
                textFile = window.URL.createObjectURL(data);
            
                return textFile;
              };
          

        var link = document.createElement('a');

        link.setAttribute('download', 'info.txt');

        link.href = makeTextFile(JSON.stringify(dados));

        document.body.appendChild(link);


        // wait for the link to be added to the document
        window.requestAnimationFrame(function () {

          var event = new MouseEvent('click');

          link.dispatchEvent(event);

          document.body.removeChild(link);
        });   

    });
});
