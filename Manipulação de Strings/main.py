url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"



url = url.strip()

if url == "":
    raise ValueError("A url está vazia")

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]


parametro_busca = 'origem'
indice_parametro = url_parametros.find(parametro_busca)

if indice_parametro != -1:
    indice_valor = indice_parametro + len(parametro_busca) + 1

else:
    raise ValueError("Parametro indiponível")

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)