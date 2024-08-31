"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.

"""
def eh_par(n1):
    return n1 % 2 == 0

n1 = int(input("digite um número inteiro."))


if eh_par(n1) :
    print(f" par ")

else: 
    print(f" impar")
