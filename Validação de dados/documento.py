from validate_docbr import CPF, CNPJ

class Documento():

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!!")

class DocCpf():
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self) -> str:
        return self.format()


    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        formatado = CPF()
        return formatado.mask(self.cpf)


class DocCnpj():
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!!")

    def __str__(self) -> str:
        return self.format()


    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        formatado = CNPJ()
        return formatado.mask(self.cnpj)

