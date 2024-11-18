import random
import time
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
def gerador_de_números(qnt_num, tam_num):
    lista = []
    while len(lista) < qnt_num:
        numeros = random.randint(0, tam_num)
        if numeros not in lista:
            lista.append(numeros)
    
    return lista
def barra_carregamento(tamanho=30, duracao=5):
    for i in range(tamanho + 1):
        porcentagem = (i / tamanho) * 100
        barra = '█' * i + '-' * (tamanho - i)
        print(f"\r[{barra}] {porcentagem:.2f}%", end="")
        time.sleep(duracao / tamanho)   

print("-=-"*50)
print("                                                   Bem-vindo ao seu sorteador de números :D")
print("-=-"*50)

qnt_num = int(input("Digite a quantidade de números que você deseja sortear: "))
tam_num = int(input("Digite o maximo de números da cartela:"))

limpar_tela()
print("calculando números")
barra_carregamento()
limpar_tela()

numeros_sorteados = gerador_de_números(qnt_num, tam_num )
contador = 0
for numero in numeros_sorteados:
    contador = contador + 1
    print(f" o {numero - numero + contador}º número: {numero}")
print("Boa-Sorte ")