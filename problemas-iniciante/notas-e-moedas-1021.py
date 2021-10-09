"""
Notas e Moedas

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule
o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50,
20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas
necessárias.

Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

"""
# Leia um valor de ponto flutuante com duas casas decimais.
valor = float(input())

# Array de notas.
notas = [100, 50, 20, 10, 5, 2]

# Array de moedas.
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Array vazio de número de notas
numeroNotas = []

# Calcule o menor número de notas possíveis no qual o valor pode ser decomposto.
for numero in notas:
    qtdValor = int(valor / numero)
    valor -= numero * qtdValor
    numeroNotas.append(qtdValor)

# Array vazio de moedas
numeroMoedas = []

# Calcule o menor número de moedas possíveis no qual o valor pode ser decomposto.
for numero in moedas:
    qtdValor = float(valor / numero)
    valor -= numero * qtdValor
    numeroNotas.append(qtdValor)

# Mostre a relação de notas e moedas necessárias.
print('NOTAS:')
print(f'{numeroNotas[0]} nota(s) de R$ 100.00')
print(f'{numeroNotas[1]} nota(s) de R$ 50.00')
print(f'{numeroNotas[2]} nota(s) de R$ 20.00')
print(f'{numeroNotas[3]} nota(s) de R$ 10.00')
print(f'{numeroNotas[4]} nota(s) de R$ 5.00')
print(f'{numeroNotas[5]} nota(s) de R$ 2.00')
