"""
A fórmula para calcular a área de uma circunferência é: área = pi.raio². Considerando para este problema que
pi = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por pi.

Entrada:
    A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

Saída:
    Apresentar a mensagem "A=" seguido pelo valo da variável area, conforme exemplo abaixo, com 4 casas após o
    ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir
    o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
"""


raio = float(input())
pi = 3.14159
area = pi * raio**2

print('A={:.4f}'.format(area))



