#importações
import string
import random

lista=[] #lista vazia para receber e imprimir numeros
pessoas=int(input("digite a quantidade de amigos: "))#recebe uma quantidade x de pessoas

for nome in range(pessoas):#repetição de nomes de acordo com a quantidade de pessoas digitada
    nome = input("Nome do Amigo(a) secreto: ")#nome dos amigos secretos
    lista.append(nome)# adicionando os amigos na lista
print(random.choice(lista))# print o amigo sorteado


