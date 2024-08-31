"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.

"""



def o_maior(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    else:
        if n2 >= n1 and n2 >= n3:
            return 2
        else:
             if n3 >= n1 and n3 >= n2:
                  return 3

def o_menor(n1, n2, n3):
       
    if n1 <= n2 and n1 <= n3:
        return n1
    else:
        if n2 <= n1 and n2 <= n3:
            return 2
        else:
             if n3 <= n1 and n3 <= n2:
                  return 3


n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

print(f" O maior número é {o_maior}")
print(f"O menor númeor é {o_menor}")


