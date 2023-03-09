import re
import config

with open(config.ARQUIVO_API) as f:
    string = f.read()

resultado = re.findall(r'[0-9]+', ' '.join(re.findall(r'"id": "[0-9]*"', string)))

resultado = ','.join(resultado) 

print(len(resultado))

f = open(config.ARQUIVO_IDS, "a")
f.write(resultado)
f.close()