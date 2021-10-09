"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

Entrada

O arquivo de entrada contém três valores inteiros.
Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

"""
import math

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior1 = (((a + b) + abs(a - b))/2)

maior2 = (((maior1 + c) + abs(maior1 - c))/2)

print('%d eh o maior' %maior2)
print('{:0} eh o maior'.format(maior2))
