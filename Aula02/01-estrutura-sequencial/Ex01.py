"""
Exercício 01 – Escreva um programa que utilize a função print() para exibir uma saudação personalizada.
Defina qualquer valor para a variável nome e idade.
O programa deve exibir: 'Ana tem 25 anos de idade'.

  
nome = "Ana"
idade = 25
"""
# Seu código aqui



nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

msg = f"{nome} tem {idade} anos."

print(msg)