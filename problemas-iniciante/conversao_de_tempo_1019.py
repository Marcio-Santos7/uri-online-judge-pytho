"""
Conversão de Tempo

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o
expresso no formato horas:minutos:segundos.

Entrada

O arquivo de entrada contém um valor inteiro N.
Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo
fornecido.

"""

# Ler o valor inteiro representando o total em segundos
valorSegundos = int(input())

# Encontrar as horas, minutos e segundos a partir do inteiro em segundos.

qtdHoras = int(valorSegundos / 3600)
valorSegundos -= qtdHoras * 3600
qtdMinutos = int(valorSegundos / 60)
valorSegundos -= qtdMinutos * 60
qtdSegundos = int(valorSegundos / 1)
valorSegundos -= qtdMinutos * 1

# imprimir o formato horas:minutos:segundos
print(f'{qtdHoras}:{qtdMinutos}:{qtdSegundos}')
