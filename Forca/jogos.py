import forca
import adivinhacao

print("*" * 28)
print("*****Escolha o seu jogo*****")
print("*" * 28)

print("(1)Forca - (2) Adivinhação")

jogo = int(input("Qual jogo: "))
print()

if jogo == 1:
    print("Jogando forca")
    forca.jogar()
else:
    print("Jogando adivinhação")
    adivinhacao.jogar()

