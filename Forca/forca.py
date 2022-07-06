import random
from random import randint

def welcome():
    print("*" * 20)
    print("Bem vindo no jogo de Forca")
    print("*" * 20)

def carrega_arquivo():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numb = random.randint(0, len(palavras) - 1)

    palavra_secreta = palavras[numb].lower()

    return palavra_secreta

def jogar():

    welcome() # Função para imprimir apresentação do jogo 

    palavra_secreta = carrega_arquivo() #Carrega palavra secreta do arquivo e armazena em uma var

    letras_acertadas = ["_" for letra in palavra_secreta] # Coloca _ para cada letra da palavra secreta

    enforcou = False
    acertou = False
    erros  = 0

    while not enforcou and not acertou:

        chute = input("Digite uma letra: ").lower()
        chute = chute.strip()

        if chute in palavra_secreta: # Testa se a contém a letra na palavra secreta
            index = 0
            for letra in palavra_secreta: # Procura a letra na palavra secreta
                if chute == letra:          
                    letras_acertadas[index] = letra # Troca "_" pela letra chutada
                index += 1
        
        else:
            erros += 1
        
        enforcou = erros == 6 # Para o jogo se tiver 6 erros
        acertou = "_" not in letras_acertadas # Ganha se não existir "_" na lista
        print(letras_acertadas)
        print(f"Ainda restam {6 - erros} tentativas")
    
    if acertou:
        print("Você ganhou")
    
    else:
        print("Perdeu")

if __name__ == "__main__":
    jogar()