class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.format_cpf()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False


    def format_cpf(self):
        fatia_cpf = self.cpf[:3]
        fatia_cpf2 = self.cpf[3:6]
        fatia_cpf3 = self.cpf[6:9]
        fatia_cpf4 = self.cpf[9:]

        return (
            f"{fatia_cpf}.{fatia_cpf2}.{fatia_cpf3}-{fatia_cpf4}"
        )