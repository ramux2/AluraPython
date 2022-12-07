from cpf import Documento
from validate_docbr import CNPJ




cpf = Documento.cria_documento("10633406910")
print(cpf)

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
