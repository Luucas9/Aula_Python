#1. crie um algoritmo para solicitar para o usuario email e senha. após isso, crie uma estrutura de condição para mostrar se o usuario terá acesso ou nao ao sistema
email_correto = 'teste@gmail.com'
senha_correta = 'senha123'

email = input("Insira o email: ")
senha = input("Insira a senha: ")

def verificar_email(email, senha):
if email == email_correto and senha == senha_correta:
print("acesso permitido")
else:
print("acesso negado")

verificar_email(email, senha)



#exercicio 2
#crie um altoritimo que solicite o salario para o usuario e mostre o valor que sera descontado, bem como o salario a ser recebido
#até 1621,00, aliquota 7,5%, parcela a deduzir(r$) -
#de 1621,00 até 2902,84, aliquota 9%, parcela a deduzir(r$) 24,32
#de 2902,85 até 4354,27, aliquota 12%, parcela a deduzir(r$) 111,40

salario = float(input("Insira o salario: "))


if salario <= 1621:
# faixa 1
aliquota = 7.5
parcela_deduzir = 0

elif 1621 < salario <= 2902.84:
# faixa 2
aliquota = 9
parcela_deduzir = 24.32
elif 2902.85 <= salario <= 4354.27:
# faixa 3
aliquota = 12
parcela_deduzir = 111.40

desconto = (salario * aliquota / 100) - parcela_deduzir

salario_final = salario - desconto

print("Desconto de R$", desconto)
print("Salario final R$", salario_final)
