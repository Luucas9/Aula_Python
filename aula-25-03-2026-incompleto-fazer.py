Exercícios

"1- Sistema de login com nível de acesso. solicite usuário e senha.
"Se usuário é igual a admin, crie uma estrutura de condição aninhada para
"solicitar senha e se a mesma for '1234', mostre que o usuário terá acesso total.
"Caso o usuário insira a senha incorreta, mostre senha incorreta.
"Caso usuário insira usuário incorreto, mostre usuário incorreto "

usuario = input("insira seu usuario: ")

if usuario == "admin":
senha = input("insira seu sua senha: ")

if senha == "1234":
print("Usuario e senha correta, bem vindo(a)!")
else:
print("Senha incorreta!")
else:
print("usuario incorreto")


2. Classificação de idade.
solicite idade, se idade for maior ou igual a 18,
crie uma estrutura de condição aninhada para verificar
se idade é maior ou igual a 60, se for, mostre que é idoso,
senão, mostre que é adulto. Se idade for maior ou igual a 12,
adolescente, caso contrário, criança.

idade = int(input("Insira sua idade: "))

if idade >= 18:
if idade >= 60:
print("Voce foi identificado como idoso")
else:
print("Voce foi identificado como adulto")
elif idade >= 12:
print("Voce foi identificado como adolescente")
else:
print("Voce foi identificado como criança")

3. Aprovação com distinção.
solicite nota, se nota for maior ou igual a 6,
crie condição aninhada para verificar se nota é maior ou igual a 9,
se for aprovado com excelência. Se nota não for maior ou igual a 9,
Aprovado. Caso contrário, reprovado.

nota = int(input("Insira sua nota: "))

if nota >= 6:
if nota >= 9:
print("Aprovado com excelencia")
else:
print("Aprovado")
else:
print("Reprovado")

4. Verificação de número.
Solicite número e verifique se é maior do que zero, se for,
crie uma estrutura de condição aninhada para verificar se este número é par,
se for, print positivo e par. Se não for, Positivo e ímpar.
Se número for igual a zero, print zero, caso contrário negativo.

numero = int(input("Insira o numero:"))

if numero > 0:


5. Sistema de desconto. solicite valor e se a pessoa é vip ou não. Se valor maior ou igual 200, crie estrutura de condição aninhada para verificar se a pessoa é vip, se for, ofereça 20% de desconto sobre o valor e mostre o valor a ser descontado e o valor final, considerando o desconto. Se não for vip, ofereça o desconto de 10%.

6. Crie um algoritmo para perguntar para o usuário qual o dia da semana, caso seja sábado, escreva dia de festa. Caso seja, domingo, pergunte sobre a condição física do usuário, se estiver com dores de cabeça, print recuperando, então, precisa descansar. Caso contrário, apenas descanse. Caso não seja sábado ou domingo, mostre trabalhando, trabalhando e trabalhando!

Ex.7 - Crie um algoritmo para solicitar a escolha do menu do café da manhã.

 

1. Eggs.

2. Pancakes

3. Wafles

4. Frutas

 

Se for eggs, pergunte qual o tipo de acompanhamento.  Se for frutas, pergunte qual o tipo de fruta e acompanhamento. Para cada caso, traga um informação com print para o usuário.
