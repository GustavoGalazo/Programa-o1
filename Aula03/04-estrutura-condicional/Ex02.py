"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual, diferente, maior ou igual, menor ou igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
10 é diferente de 5.
10 é maior ou igual a 5.
10 não é menor ou igual a 5.

"""

def eh_maior(n1, n2):
    return n1 > n2

def eh_menor(n1, n2):
    return n1 < n2

def eh_igual(n1, n2):
    return n1 == n2


n1 = int(input("Digite o primeiro número: "))

n2 = int(input("Digite o segundo número:"))

if eh_maior(n1, n2):
    print(f"{n1} é maior que {n2}")

else:
    print(f"{n1} não é maior que {n2}")

    
if eh_menor(n1, n2):
    print(f"{n1} é menor que {n2}")

else:
    print(f"{n1} não é menor que {n2}")

if eh_igual(n1, n2):
    print(f"{n1} é igual a {n2}")

else:
    print(f"{n1} não é igual a {n2}")

    