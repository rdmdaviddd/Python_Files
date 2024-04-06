import matplotlib.pyplot as plt
anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
investimento = [2, 3, 6, 11,8, 12, 15, 7]
plt.plot(anos, investimento) #criando gráfico com eixos x e y
plt.title("Investimento em Tecnologia") #criando título do gráfico
plt.ylabel("Milhões de R$") #rótulo ao eixo y
plt.xlabel("Década") #rótulo ao eixo x
plt.show #exibir gráfico