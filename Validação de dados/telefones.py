import re

class Telefones:
    def __init__(self, telefone) -> None:
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número Incorreto")
        
    def valida(self, telefone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        resposta = re.findall(pattern, telefone)

        if resposta:
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.formata()

    def formata(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(pattern, self.numero)
        numero_formatado = f"+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado