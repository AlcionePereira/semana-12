# Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês.
# Você deseja comprar um carro,mas o preço do carro sobe a taxa de 0,4% ao mês.
# Escreva um programa que leia o preço de um carro hoje e calcule em
# quantos meses,com o dinheiro dessa aplicação, você terá dinheiro suficiente
# para comprar o carro à vista.

carro = float(input().strip())
poup = 10000
rende = 0.007
taxa = 0.004
mes = 0

while poup <= carro: 
    poup = poup + poup * rende 
    carro = carro + carro * taxa 
    mes+=1
    

print(mes)

