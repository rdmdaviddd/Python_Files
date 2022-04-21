#Programa recebe numero inteiro na entrada e verifica se o numero recebido possui ao menos um digito
#adjacente igual a ele.
n = input("Digite um número inteiro")#entrada usuario
d = int (len(n))#funçao len pega tamanho da entrada ja convertendo para inteiro (quant. algarismos do numero)
n = int(n)#converte numero inserido para inteiro 
c = 1 #inicializador do contador
y = 0 #utilizada como fator multiplicador para separada dos algarismos variando de acordo com a quantidade de algarismos do numero inserido 
r = 0 #variavel referente ao digito anterior 
r1 = 0#variavel referente ao digito seguinte 
adj = False #indicador de passagem
while (c <= d):#contador
      x = 10**y #variavel utilizada para formula de separação dos algarismos
      y = y + 1 #y varia de acordo com a quant. de algarismos do numero de entrada
      c = c + 1
      r = (( n // x ) % 10)# formula de separação dos algarismos
      if(d>1): #testa pq a função tem que ter pelos menos dois algarismos inseridos para comparação
             a = 10**y 
             r1 = (( n // a ) % 10)
             
             if(r == r1):#realiza comparação
                 adj = True
                 c = d + 1 #para o contador se o indicador de passagem encontrar a condição
             
if(adj == True):#imprime de acordo a condição do indicador de passagem
      print ("SIM")
             
if(adj == False):
      print ("NAO")



      
            
            
            


            
            

