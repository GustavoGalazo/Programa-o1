"""
Exercício 04 - Escreva um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
A fórmula de conversão é F = C * 9/5 + 32.

Exemplo de Entrada:
Digite uma temperatura em Celsius para conversão: 25

Exemplo de Saída:
25°C é equivalente a 77.0°F
"""
temp1 = float(input("Digite a temperatura em Celsius: "))

temp2 = temp1 * 9/5 + 32

msg = f"{temp1}º é equivalente a {temp2}ºF"

print(msg)