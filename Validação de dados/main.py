from datas import DatasBr
from cep import BuscaEndereco
import requests



cep = 83608150

objeto_cep = BuscaEndereco(cep)


bairro, cidade, uf = objeto_cep.acessa_API()

print(bairro, cidade, uf)