# 1) Escreva um algoritmo que armazene em um vetor e imprima os números de
# 1(inclusive) a 10(inclusive) em ordem decrescente, utilizando vetores.

valores = []
for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
valores.sort(reverse=True)
for numero in valores:
    print(numero)

# 2) Escreva um algoritmo que armazene em um vetor e imprima os 10 números
# pares que sejam menores que 20.

valores = []
for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
pares = []
for numero in valores:
    if numero % 2 == 0 and numero < 20:
        pares.append(numero)
pares.sort(reverse=True)
for par in pares[:10]:
    print(par)
#ta funcionando

# 3) Escreva um algoritmo que armazene 6 valores em um vetor e mostre o
# menor e o maior deles.

valores = []    

for i in range(6):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
    mvalor=min(valores)

print("O menor valor armzenado foi: ",mvalor,"")


# 4) Escreva um algoritmo em que receba dez números do usuário e armazene
# em um vetor a metade de cada número. Após isso, o algoritmo deve imprimir
# todos os valores armazenados.

valores = []

for i in range(3):
    valor = int(input("Digite um valor: "))
    valores.append(valor/2)
print(valores)


# 5) Escreva um algoritmo que armazene em um vetor todos os números
# múltiplos de 5, no intervalo fechado de 1 a 500. Após isso, o algoritmo deve
# imprimir todos os valores armazenados.

valores = []

for i in range(1, 501):
    if i % 5 == 0:
        valores.append(i)
print(valores)