class Cliente:

    def __init__(self, nome):
        self.__nome = nome # Precisa de __ para utilizar @property

    @property # Chama o método sem precisar utilizar ()
    def nome(self):
        return self.__nome.title()

    @nome.setter # Definir um novo nome utilizando o metodo nome()
    def nome(self, nome):
        self.__nome = nome