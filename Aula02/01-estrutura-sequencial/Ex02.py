"""
Exercício 02 – Crie um programa que exibe a soma de dois números inteiros.
Saída esperada: 'A soma de 20 e 25 é 45.'


num1 = 10
num2 = 25
"""
# Seu código aqui

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

soma = num1 + num2

msg = f"A soma de {num1} + {num2} é igual a {soma}"

print(msg)