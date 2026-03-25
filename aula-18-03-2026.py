#ex 1. - força = massa x aceleração

forca = float(input("Insira o valor da força (N): "))
aceleracao = float(input("Insira o valor da aceleração : "))

massa = forca / aceleracao

print(f"Com a força de {forca} e a aceleração de {aceleracao}, teremos a massa de {massa}")

#ex 2. estrutura de condição:
#>= 5 - massa requerida
#< 5 - não requerida
if massa >= 5:
print("Massa maior ou igual a 5")
else:
print("Massa menor que 5")
########################################################

#ex 3 - nome e cpf precisam estar ambas corretas

nome = str(input("Digite seu nome:"))
cpf = int(input("Digite seu cpf:"))

if nome == 'lucas' and cpf == 12345:
print("Acesso permitido")
else:
print("Acesso negado")

##############################

#ex 4
#um pode estar errado e outro certo que vai dar acesso permitido

nome = str(input("Digite seu nome:"))
cpf = int(input("Digite seu cpf:"))

if nome == 'lucas' or cpf == 12345:
print("Acesso permitido")
else:
print("Acesso negado")

###################################
#ex 5
nome = str(input("Digite seu nome:"))
cpf = int(input("Digite seu cpf:"))
ticket = int(input("Insira o tipo do seu ticket (1-vip, 0-comum): "))

if nome == 'lucas' and cpf == 12345 and ticket == 1:
print("Acesso ao camarote!")

elif nome == 'lucas' and cpf != 12345 and ticket == 1:
print("Precisa conversar com o gerente!")

else:
print("Acesso arquibancada!")

###########################################
#ex 6 - crie um algoritmo para solicitar renda e se tem dependente, e mostre
#beneficio aprovado, caso renda seja <= 2000 e tenha dependente, caso contrario beneficio negado
#negado

renda = int(input("Digite sua renda:"))
dependentes = int(input("Quantos dependentes possui? "))

if renda <= 2000 and dependentes >= 1:
print("Beneficio aprovado cumpanheiro")
elif renda >= 2000 and dependentes == 0:
print("Beneficio negado, faz o L")
elif renda > 2001 or dependentes >= 1:
print("Fala com o governo")

#####################

#ex 7
#crie um algoritmo para falar se a temperatura está agradavel
#ou nao, se estiver entre >=18 e <=30 - agradavel, caso contrario, nao ta agradavel

temperatura = int(input("Digite a temperatura:"))

if temperatura >= 18 and temperatura <= 30:
print("Temperatura está boa")

else:
print("Temperatura ta ruim")

#ex 8 crie um algoritmo para mostrar se um aluno ta ou nao reprov
#se tiver com nota >= 6 e frequencia >= 75 aprovado, caso contrario reprov

nota = int(input("Digite a nota:"))
frequencia = int(input("Digite a frequencia:"))

if nota >= 6 and frequencia >= 75:
print("O aluno está aprovado")

elif nota < 6 and frequencia <= 75:
print("Aluno está reprovado")

elif nota >= 6 and frequencia < 75:
print("Aluno está reprovado")

elif nota < 6 and frequencia >= 75:
print("Aluno está de recuperação")

#ex 9 - verifique se um numero é par ou impar, em função do numero escolhdo pelo usuario

numero = int(input("Digite um número: "))

# verifica se é par ou ímpar
if numero % 2 == 0:
print("O número é par")
else:
print("O número é ímpar")

#ex 10 - crie um algoritmo para falar se uma pessoa é uma criança, jovem ou adulto ou idoso
#idade < 14 - criança
#14 <= idade <18 - jovem
#18 <= idade <60 - adulto
#idade > 60 - idoso

idade = int(input("Digite sua idade: "))

if idade < 14:
print("Voce é criança")
elif idade >= 14 and idade <= 18:
print("Voce é jovem")
elif idade >= 18 and idade <= 60:
print("Voce é adulto")
elif idade >= 60 and idade <= 100:
print("Voce é idoso")
elif idade > 100:
print("Parente do peter do ei nerd")