# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:39:56 2026

@author: labsfiap
"""

1 - crie um altoritimo para verificar se um numero é verdadeiro


2 - crie um altoritmo para verificar se um numer é falso, se sim
print(faça alguma coisa) senao faça outra coisa, utulize estrutura com true ou false

numero = int(input("Digite um número: "))

condicao = False

if numero == 0:
    condicao = True
else:
    condicao = False

if condicao == True:
    print("faça alguma coisa")
else:
    print("faça outra coisa")
    
3 - solicite temperarutra para o usuario, crie uma condição temperatura < 18 e insira em uma
variavel, após isso utulize a estrutura booleana ( true ou false ) para criar a condição, se menor
do 18 est´frio, senao, nao esta frio

temperatura = int(input('Digite a temperatura: '))

esta_frio = (temperatura < 18)

if esta_frio == True:
    print("Está frio!")
else:
    print("Não está frio!")
    
    
4 - solicite para o usuario uma senha, em seguida, crie uma variavel para inserir a seguinte
condição senha = '1234'. se a informação for correta, print senha correta, caso contrario
senha incorreta

senha = int(input('Digite a senha: '))

senha_correta = (senha == 1234)

if senha_correta == True:
    print("A senha está correta!")
else:
    print("A senha está incorreta!")


5 - crie um algoritmo para solicitar um numero e verifique se o numero é par ou impar. 
porem, crie uma variavel com a condição

numero = int(input("Digite o numero: "))

divisivel = (numero % 2 == 0)

if divisivel == True:
    print(f"O numero {numero} inserido é par!")
else:
    print(f"O numero {numero} inserido é impar!")
    
6 - crie um altoritimo que solicite o salario para o usuario. apos isso, crie 4 condições
a) se o salario for até 2000, não tera desconto. entrao mostre o salario a ser recebibo
b) se o salario for maior do que 2000 e até 3500. o funcionario terá 10% de desconto
c) se o salario for maior do que 3500 e até 5000. o funcionario terá 20% de desconto
b) se o salario for maior do que 5000. o funcionario terá 27,5% de desconto
    

salario = float(input("Digite o salário: "))

faixa1 = (salario <= 2000)
faixa2 = (salario > 2000 and salario <= 3500)
faixa3 = (salario > 3500 and salario <= 5000)
faixa4 = (salario > 5000)

if faixa1 == True:
    desconto = 0
elif faixa2 == True:
    desconto = 0.10
elif faixa3 == True:
    desconto = 0.20
else:
    desconto = 0.275

salario_final = salario - (salario * desconto)

print(f"Salário final: R$ {salario_final:.2f}")
