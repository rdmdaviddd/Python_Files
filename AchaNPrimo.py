#Programa recebe numero inteiro positivo na entrada e verifica se é primo ou não.

n = int (input("Digite um número inteiro"))
c=1
x = 1
y = 0
v = 0
while (c <= n):
       x = n % c
       print(x)
       c = c+1
       if(x==0):
          y = y + 1
          print (y)
if(n==0 or n==1 or y > 2):
   print ("não primo")
else:
    print ("primo")



    












     
  


