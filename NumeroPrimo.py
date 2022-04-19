#Escreva um programa que receba um número inteiro positivo na entrada
#e verifique se é primo.Se o número for primo, imprima "primo".
#Caso contrário, imprima "não primo".
n = int (input("Digite um numero inteiro não negativo"))
if (n == 0 or n == 1) or ( n != 2 and n % 2 == 0):
    print("nao primo")
else:
     print("numero primo")     



