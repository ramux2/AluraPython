class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor
    
    def libera_saque(self, valor_p_sacar):
        
    
    def saque(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor  
        else:
            print(f"O valor {valor}passou o limite")

    def ted(self, conta2, valor):
        self.saque(valor)
        conta2.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite