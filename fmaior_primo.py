def eprimo(k):#função que verifica se o numero é primo
    c = 1
    x = 1
    y = 0
    primo = True
    while (c <= k):
         x = k % c
         c = c+1
         if(x==0):
           y = y + 1
    if(y > 2 or k == 0 or k == 1):
       primo = False
    return(primo)

def maior_primo(n):#função que verifica qual é o maior numero primo
   
    c = 0
    while (c <= n):
         q = eprimo(c)#q é igual o numero inserido pelo usuario sendo que e testado todos numeros anteriores
          
         c = c + 1
         if(q==True):#retira para variavel a apenas os casos de verdadeiro para positivo
            a = c - 1
            
    
    if(n >= 2):#retorna o maior numero primo encontrado
       return a
    else:
        return ("Não tem primo")
    
         


    
