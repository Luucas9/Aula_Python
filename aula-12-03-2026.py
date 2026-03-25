V = X I

V = tensão
R = resistencia
I = corrente

# Calculo da resistencia do carregaor de celular
# variáveis

V = 5
I = 0.5

# equação
R = V / I
print("O valor da resistencia do carregador é: ", R)
###############################

#ex 2

V = float(input("Digite o valor de V: "))
I = float(input("Digite o valot de I: "))

#EQUAÇÃO
R = V / I
print("O valor da resistencia do carregador é: ", R)

####################################
#ex 3 - equação do segundo grau
x = float(input("Digite o valor de x: "))
resultado = (10 * x**2) + (5*x) + 2
print(f"O resultado desta equação será: {resultado}")
#10x**2 * 5x + 2

############################################
#ex 4 - Transformar temperatura fahrenheit para Graus Celsius

#C = (F - 32) / 1.8

Fahr = float(input("Digite o valor em Fahrenheit: "))
celsius = (Fahr - 32) / 1.8

print(f"O valor em Fahrenheit é: {Fahr}")
print(f"O valor em Celsius é: {celsius}")

#############################################

#Ex.5 - Calcular o valor de E dado a equação é:
# E = m*C**2

m = float(input("digite o valor de m (massa): "))
C = float(input("digite o valor de c (velocidade da luz): "))

E = m*C**2

print(f"O valor de massa é: {m}")
print(f"O valor da velocidade da luz é: {C}")
print(f"O valor da energia é: {E}")

###########################

#Ex 6

#exercicio 6
#crie um altoritimo que solicite o salario para o usuario e mostre o valor que sera descontado, bem como o salario a ser recebido
#até 1621,00, aliquota 7,5%, parcela a deduzir(r$) -
#de 1621,00 até 2902,84, aliquota 9%, parcela a deduzir(r$) 24,32
#de 2902,85 até 4354,27, aliquota 12%, parcela a deduzir(r$) 111,40

salario = float(input("digite o salario "))

# Estrutura de condição:
if salario <= 1621.00:
aliquota = 7.5
parcela_deduzir = 0
elif salario <= 2902.84:
aliquota = 9
parcela_deduzir = 24.32
elif 2902.84 < salario <= 4354.27:
aliquota = 12
parcela_deduzir = 111.40

else:
print("Salario fora da tabela")
exit()

desconto = (salario * aliquota / 100) - parcela_deduzir

salario_final = salario - desconto

print(f"O salario primário: {salario}")
print(f"O aliquota é: {aliquota}")
print(f"A parcela a deduzir é: {parcela_deduzir}")
print(f"O desconto foi: {desconto}")
print(f"salario final é = {salario_final}") 