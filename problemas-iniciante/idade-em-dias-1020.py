"""
Idade em Dias

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste
nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com
objetivo de testar raciocínio matemático simples.

Entrada

O arquivo de entrada contém um valor inteiro.

Saída

Imprima a saída conforme exemplo fornecido.

"""
# Ler um valor inteiro representando o número de dias de vida de uma pessoa.

diasVida = int(input())

# Array com anos, meses  e dias em dias

numerosDias = [365, 30, 1]

# Iterar sobre o array para encontrar a conversão para anos, meses e dias.
listaFormato = []
for dia in numerosDias:
    qtdDias = int(diasVida / dia)
    diasVida -= dia * qtdDias
    listaFormato.append(qtdDias)

# Imprimir o formato anos, meses e dias.

print(f'{listaFormato[0]} ano(s)')
print(f'{listaFormato[1]} mes(es)')
print(f'{listaFormato[2]} dia(s)')
