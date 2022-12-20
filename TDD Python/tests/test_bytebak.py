from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):

        entrada = "13/03/2000" # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade() # When-Ação

        assert resultado == esperado #Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):

        entrada = "Lucas Carvalho" # Given-Contexto
        esperado = "Carvalho"

        lucas = Funcionario(entrada, "11/11/2000", 11111)

        resultado = lucas.sobrenome()# When-Ação

        assert resultado == esperado  

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #Given
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/03/2000", entrada_salario)

        funcionario_teste.decrescimo_salario() #When

        resultado = funcionario_teste._salario

        assert resultado == esperado #Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 #Given
        entrada_nome = "Ana"
        esperado = 100

        ana_teste = Funcionario(entrada_nome, "11/03/1997", entrada_salario)
        resultado = ana_teste.calcular_bonus() #When

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_x_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000000 #Given
            entrada_nome = "Ana"

            ana_teste = Funcionario(entrada_nome, "11/03/1997", entrada_salario)
            resultado = ana_teste.calcular_bonus() #When

            assert resultado