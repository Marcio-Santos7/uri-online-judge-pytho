"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a
ser pago.

Entrada

O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros
e um valor com 2 casas decimais.

Saída

A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os
dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

"""
codPeca1, quantPeca1, valorPeca1 = input().split()
codPeca2, quantPeca2, valorPeca2 = input().split()

codPeca1 = int(codPeca1)
quantPeca1 = int(quantPeca1)
valorPeca1 = float(valorPeca1)

codPeca2 = int(codPeca2)
quantPeca2 = int(quantPeca2)
valorPeca2 = float(valorPeca2)

valorTotal = ((quantPeca1 * valorPeca1) + (quantPeca2 * valorPeca2))

print('VALOR A PAGAR: R$ {:.2f}'.format(valorTotal))
